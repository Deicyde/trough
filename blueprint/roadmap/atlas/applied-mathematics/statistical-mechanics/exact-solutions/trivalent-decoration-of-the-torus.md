---
declaration: section
origin: cited
lean: StatMech.Onsager.ons_spinVertexGauge, StatMech.Onsager.ons_spinDartSeamSign, StatMech.Onsager.ons_spinSeamDecWeight, StatMech.Onsager.ons_diagonalGaugeMatrix, StatMech.Onsager.ons_decMiddleStateGauge, StatMech.Onsager.ons_decInternalAdj, StatMech.Onsager.ons_decAdj, StatMech.Onsager.ons_decGraph
statement: formalized
proof: formalized
---

# Trivalent decoration of the torus

90 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html).

## Spin boundary-phase gauge at a site

The gauge `u^{s₁} v^{s₂}` at site `s`, with `u, v` the spin boundary phases.

Formalized by `StatMech.Onsager.ons_spinVertexGauge`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationSpinGauge.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationSpinGauge.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-spin-vertex-gauge).

## Seam sign of a dart

The seam sign
`(-1)^{a · (signed vertical seam crossing) + b · (signed horizontal seam crossing)}` of a dart.

Formalized by `StatMech.Onsager.ons_spinDartSeamSign`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationSpinGauge.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationSpinGauge.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-spin-dart-seam-sign).

## Decorated weights twisted by seam signs

Decorated weights with every external edge multiplied by the seam sign of its dart.

Formalized by `StatMech.Onsager.ons_spinSeamDecWeight`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationSpinGauge.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationSpinGauge.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-spin-seam-dec-weight).

## Diagonal gauge conjugation of a matrix

Diagonal conjugation `gauge i * M i j * (gauge j)⁻¹`.

Formalized by `StatMech.Onsager.ons_diagonalGaugeMatrix`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationSpinGauge.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationSpinGauge.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-diagonal-gauge-matrix).

## Gauge on the states of the augmented matrix

The gauge on the states of the augmented matrix: the site gauge on darts, and the gauge of
`site` on the two side states.

Formalized by `StatMech.Onsager.ons_decMiddleStateGauge`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationSpinGauge.lean, line 436](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationSpinGauge.lean#L436). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-middle-state-gauge).

## Internal adjacency of the torus decoration

Internal adjacency of the decoration: two darts at the same site whose directions are
consecutive in `0, 1, 2, 3`.

Formalized by `StatMech.Onsager.ons_decInternalAdj`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusDecoration.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusDecoration.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-internal-adj).

## Adjacency of the decorated torus graph

Adjacency of the decorated graph: a dart is joined to its reverse and to its internal neighbors.

Formalized by `StatMech.Onsager.ons_decAdj`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusDecoration.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusDecoration.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-adj).

## Decorated graph of the torus

The decorated graph of the torus: vertices are darts, external edges join each dart to its
reverse, and internal edges form the path `(s, 0) - (s, 1) - (s, 2) - (s, 3)` at each site `s`.

Formalized by `StatMech.Onsager.ons_decGraph`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusDecoration.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusDecoration.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-graph).

## Internal neighbors of a dart in the decoration

The internal neighbors of a dart in the path at its site.

Formalized by `StatMech.Onsager.ons_decInternalNeighbors`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusDecoration.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusDecoration.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-internal-neighbors).

## Internal-edge bits completing port bits at a site

The internal-edge bits `(b₀, b₀ + b₁, b₀ + b₁ + b₂)` that complete port bits `b₀, …, b₃` at one
site to an even subgraph.

Formalized by `StatMech.Onsager.ons_decChainCompletion`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusDecoration.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusDecoration.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-chain-completion).

## Parity condition of the decoration at one site

Parity of the decorated subgraph at the four darts of one site, for port bits `b₀, …, b₃` and
internal-edge bits `y`.

Formalized by `StatMech.Onsager.ons_decChainEven`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusDecoration.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusDecoration.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-chain-even).

## Port pattern on the darts of the torus

A port pattern: one bit per dart, equal on a dart and its reverse, with an even number of ones
at each site. Port patterns encode even subgraphs of the torus.

Formalized by `StatMech.Onsager.ons_PortPattern`, a structure declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusDecoration.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusDecoration.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-port-pattern).

## Internal-edge bits at a site from a port pattern

The internal-edge bits at a site determined by a port pattern.

Formalized by `StatMech.Onsager.ons_portChainBit`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusDecoration.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusDecoration.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-port-chain-bit).

## Port-pattern bit of the decorated edge between two darts

The bit of the decorated edge between `d` and `e` determined by a port pattern.

Formalized by `StatMech.Onsager.ons_decNeighborBit`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusDecoration.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusDecoration.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-neighbor-bit).

## Port-pattern bit of an unordered decorated edge

The bit of a decorated edge determined by a port pattern.

Formalized by `StatMech.Onsager.ons_decEdgeBit`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusDecoration.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusDecoration.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-edge-bit).

## Even decorated subgraph determined by a port pattern

The even subgraph of the decorated graph determined by a port pattern.

Formalized by `StatMech.Onsager.ons_decoratedEdges`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusDecoration.lean, line 266](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusDecoration.lean#L266). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-decorated-edges).

## Torus edge underlying a dart

The torus edge underlying a dart.

Formalized by `StatMech.Onsager.ons_portEdge`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusDecoration.lean, line 405](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusDecoration.lean#L405). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-port-edge).

## Port bit of a dart for a torus edge set

The bit of a dart in the port pattern of an edge set `F`: `1` if its underlying torus edge lies
in `F`.

Formalized by `StatMech.Onsager.ons_portBit`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusDecoration.lean, line 494](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusDecoration.lean#L494). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-port-bit).

## Port pattern of an even subgraph of the torus

The port pattern of an even subgraph of the torus.

Formalized by `StatMech.Onsager.ons_evenSubgraphPortPattern`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusDecoration.lean, line 499](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusDecoration.lean#L499). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-even-subgraph-port-pattern).

## Port bit of a dart in a decorated edge set

The port bit of a dart in a decorated edge set: whether the external edge at the dart is
present.

Formalized by `StatMech.Onsager.ons_decoratedPortBit`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusDecoration.lean, line 533](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusDecoration.lean#L533). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-decorated-port-bit).

## Internal-edge bits of a decorated edge set at a site

The three internal-edge bits of a decorated edge set at one site.

Formalized by `StatMech.Onsager.ons_decoratedChainBits`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusDecoration.lean, line 538](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusDecoration.lean#L538). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-decorated-chain-bits).

## Port pattern of an even decorated subgraph

The port pattern of an even subgraph of the decorated graph.

Formalized by `StatMech.Onsager.ons_portPatternOfDecorated`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusDecoration.lean, line 601](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusDecoration.lean#L601). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-port-pattern-of-decorated).

## Torus edge set of a port pattern

The torus edge set of a port pattern.

Formalized by `StatMech.Onsager.ons_portPatternEdges`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusDecoration.lean, line 798](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusDecoration.lean#L798). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-port-pattern-edges).

## Equivalence between even torus subgraphs and port patterns

Even subgraphs of the torus are equivalent to port patterns.

Formalized by `StatMech.Onsager.ons_evenSubgraphPortEquiv`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusDecoration.lean, line 910](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusDecoration.lean#L910). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-even-subgraph-port-equiv).

## Equivalence between even decorated subgraphs and port patterns

Even subgraphs of the decorated graph are equivalent to port patterns.

Formalized by `StatMech.Onsager.ons_decoratedPortEquiv`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusDecoration.lean, line 932](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusDecoration.lean#L932). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-decorated-port-equiv).

## Equivalence between even subgraphs of the torus and its decoration

Even subgraphs of the torus are equivalent to even subgraphs of the decorated graph.

Formalized by `StatMech.Onsager.ons_decorationEquiv`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusDecoration.lean, line 941](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusDecoration.lean#L941). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-decoration-equiv).

## Offset of a dart inside its 8 × 8 cell

The offset of a dart in direction `μ` inside its `8 × 8` cell: east `(6, 4)`, north `(4, 6)`,
west `(2, 4)`, south `(4, 2)`.

Formalized by `StatMech.Onsager.ons_decEmbedOffset`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationEmbedding.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationEmbedding.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-embed-offset).

## Position of a dart in the 8L × 8L torus

The position `8 s + offset(μ)` of the dart `(s, μ)` in the `8L × 8L` torus.

Formalized by `StatMech.Onsager.ons_decEmbedVertex`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationEmbedding.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationEmbedding.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-embed-vertex).

## Step directions of the route of a decorated edge

The four step directions of the route of the decorated edge from `d` to `e`: straight for an
external edge, an L-shaped turn for an internal edge.

Formalized by `StatMech.Onsager.ons_decEdgeRouteDirs`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationEmbedding.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationEmbedding.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-edge-route-dirs).

## Endpoint of four lattice steps

The endpoint of four lattice steps in the given directions.

Formalized by `StatMech.Onsager.ons_fourDirSteps`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationEmbedding.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationEmbedding.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-four-dir-steps).

## Torus walk of four lattice steps

The torus walk of four lattice steps in the given directions.

Formalized by `StatMech.Onsager.ons_fourDirStepWalk`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationEmbedding.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationEmbedding.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-four-dir-step-walk).

## Finer 8L × 8L torus graph for the decorated graph

The `8L × 8L` torus graph in which the decorated graph is drawn.

Formalized by `StatMech.Onsager.ons_decEmbedGraph`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationEmbedding.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationEmbedding.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-embed-graph).

## Four-step route of a decorated edge in the finer torus

The four-step route of the decorated edge from `d` to `e` in the finer torus.

Formalized by `StatMech.Onsager.ons_decEdgeRoute`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationEmbedding.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationEmbedding.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-edge-route).

## Five points of the route of a decorated edge

The five points of the route of the decorated edge from `d` to `e`.

Formalized by `StatMech.Onsager.ons_decEdgeRouteVertices`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationEmbedding.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationEmbedding.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-edge-route-vertices).

## Micro point of the finer torus as a cell and an offset

A point of the `8L × 8L` torus given as a coarse cell and an offset in `Fin 8 × Fin 8`.

Formalized by `StatMech.Onsager.ons_DecMicroPoint`, a structure declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationEmbedding.lean, line 415](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationEmbedding.lean#L415). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-micro-point).

## Point of the finer torus represented by a micro point

The point of the finer torus represented by a micro point.

Formalized by `StatMech.Onsager.ons_decMicroVertex`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationEmbedding.lean, line 422](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationEmbedding.lean#L422). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-micro-vertex).

## Interior points of the route of a decorated edge

The three interior points of the route of the decorated edge from `d` to `e`, as micro points.

Formalized by `StatMech.Onsager.ons_decEdgeInteriorData`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationEmbedding.lean, line 473](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationEmbedding.lean#L473). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-edge-interior-data).

## Decorated edge whose route passes through an interior micro point

The decorated edge whose route passes through a given interior micro point.

Formalized by `StatMech.Onsager.ons_decMicroCorridorEdge`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationEmbedding.lean, line 517](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationEmbedding.lean#L517). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-micro-corridor-edge).

## Cell offsets used by interior route points

The offsets inside a cell used by interior points of routes.

Formalized by `StatMech.Onsager.ons_decInteriorOffsets`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationEmbedding.lean, line 619](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationEmbedding.lean#L619). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-interior-offsets).

## Micro point at which a dart is placed

The micro point at which a dart is placed.

Formalized by `StatMech.Onsager.ons_decPortMicroPoint`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationEmbedding.lean, line 642](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationEmbedding.lean#L642). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-port-micro-point).

## Route points of a decorated edge after its start

The points of the route of a decorated edge after its starting point.

Formalized by `StatMech.Onsager.ons_decDartSegment`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationEmbedding.lean, line 695](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationEmbedding.lean#L695). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-dart-segment).

## Image of a decorated walk in the finer torus

The image of a decorated walk in the finer torus, obtained by concatenating the routes of its
edges.

Formalized by `StatMech.Onsager.ons_decEmbedWalk`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationEmbedding.lean, line 737](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationEmbedding.lean#L737). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-embed-walk).

## Four finer-torus darts along the route of a decorated edge

The four darts of the finer torus along the route of the decorated edge from `d` to `e`.

Formalized by `StatMech.Onsager.ons_decEdgeMicroDarts`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationEmbeddingTurns.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationEmbeddingTurns.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-edge-micro-darts).

## Expanded dart list of a decorated walk in the finer torus

The darts of the finer torus along the image of a decorated walk.

Formalized by `StatMech.Onsager.ons_decExpandedDartList`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationEmbeddingTurns.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationEmbeddingTurns.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-expanded-dart-list).

## First dart of the expanded dart list of a decorated cycle

The first dart of the expanded dart list of a decorated cycle.

Formalized by `StatMech.Onsager.ons_decExpandedRoot`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationEmbeddingTurns.lean, line 405](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationEmbeddingTurns.lean#L405). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-expanded-root).

## Expanded loop of a decorated cycle in walking order

The expanded dart list of a decorated cycle as a cyclic sequence, in walking order.

Formalized by `StatMech.Onsager.ons_decExpandedGeometricLoop`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationEmbeddingTurns.lean, line 456](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationEmbeddingTurns.lean#L456). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-expanded-geometric-loop).

## Expanded loop of a decorated cycle in Kac-Ward order

The expanded dart list of a decorated cycle as a cyclic sequence in Kac-Ward order (reversed
indexing).

Formalized by `StatMech.Onsager.ons_decExpandedKWLoop`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationEmbeddingTurns.lean, line 575](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationEmbeddingTurns.lean#L575). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-expanded-kwloop).

## Internal edge of the path at a site

The `i`-th internal edge `(s, i) - (s, i + 1)` of the path at a site.

Formalized by `StatMech.Onsager.ons_decChainEdge`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationTransitionWeights.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationTransitionWeights.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-chain-edge).

## Indices of internal edges between two ports

The indices of the internal edges on the path between ports `a` and `b` at one site.

Formalized by `StatMech.Onsager.ons_decChainPathIndices`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationTransitionWeights.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationTransitionWeights.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-chain-path-indices).

## Internal edges between two ports at a site

The internal edges on the path between ports `a` and `b` at a site.

Formalized by `StatMech.Onsager.ons_decChainPathEdges`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationTransitionWeights.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationTransitionWeights.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-chain-path-edges).

## Decorated weight of a Kac-Ward transition

The decorated weight of the Kac-Ward transition from `d₁` to `d₂`: the weight of the external
edge at `d₁` times the weights of the internal edges from the port of `d₁ + 2` to the port of `d₂`.

Formalized by `StatMech.Onsager.ons_decTransitionWeight`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationTransitionWeights.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationTransitionWeights.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-transition-weight).

## Twisted Kac-Ward matrix with decorated transition weights

The twisted Kac-Ward matrix with decorated transition weights.

Formalized by `StatMech.Onsager.ons_KWmatDecorationWeightedPhase`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationTransitionWeights.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationTransitionWeights.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-kwmat-decoration-weighted-phase).

## Decorated weights induced by torus edge weights

Decorated weights induced by torus edge weights: external edges get the weight of their torus
edge, internal edges get `1`.

Formalized by `StatMech.Onsager.ons_decSpecializedWeight`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationTransitionWeights.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationTransitionWeights.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-specialized-weight).

## Decorated weights with internal edges weighted by t

Decorated weights with external edges weighted by their torus edge and internal edges by `t`.

Formalized by `StatMech.Onsager.ons_decInterpolatedWeight`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationTransitionWeights.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationTransitionWeights.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-interpolated-weight).

## Decorated character sum with weights on all edges

The decorated character sum `∑_D χ_{a,b}(hom D) ∏_{e ∈ D} w_e` with a weight on every decorated
edge.

Formalized by `StatMech.Onsager.ons_decoratedFullWeightedSpinSum`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationTransitionWeights.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationTransitionWeights.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-decorated-full-weighted-spin-sum).

## Side of a direction at a site

The side of a direction at a site: `0` for east and north, `1` for west and south.

Formalized by `StatMech.Onsager.ons_decMiddleSide`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationInternalMiddle.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationInternalMiddle.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-middle-side).

## Representative direction of a side

The representative direction of a side: east for side `0`, west for side `1`.

Formalized by `StatMech.Onsager.ons_decMiddleDir`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationInternalMiddle.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationInternalMiddle.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-middle-dir).

## Destination-side internal weight to a port

The weight of the internal edges between the middle edge and the port of direction `μ`, on the
destination side.

Formalized by `StatMech.Onsager.ons_decMiddleDestFactor`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationInternalMiddle.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationInternalMiddle.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-middle-dest-factor).

## Source-side internal weight from a port

The weight of the internal edges between the port of direction `μ` and the middle edge, on the
source side.

Formalized by `StatMech.Onsager.ons_decMiddleSourceFactor`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationInternalMiddle.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationInternalMiddle.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-middle-source-factor).

## Column factor of the rank-two middle-edge term

The column factor of the rank-two term: from a side of `site` to the darts leaving `site` on
that side.

Formalized by `StatMech.Onsager.ons_decMiddleU`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationInternalMiddle.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationInternalMiddle.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-middle-u).

## Row factor of the rank-two middle-edge term

The row factor of the rank-two term: from the darts entering `site` to the side on which they
arrive.

Formalized by `StatMech.Onsager.ons_decMiddleV`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationInternalMiddle.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationInternalMiddle.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-middle-v).

## Augmented Kac-Ward matrix with two side states

The augmented Kac-Ward matrix on darts and the two sides of `site`, with blocks `Λ₀`, `U`, `t V`
and `0`.

Formalized by `StatMech.Onsager.ons_decMiddleAugmented`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationInternalMiddle.lean, line 332](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationInternalMiddle.lean#L332). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-middle-augmented).

## Balanced augmented Kac-Ward matrix

The augmented matrix with blocks `Λ₀`, `(t λ) U`, `λ⁻¹ V` and `0`.

Formalized by `StatMech.Onsager.ons_decMiddleBalanced`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationMiddleBalanced.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationMiddleBalanced.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-middle-balanced).

## Row weights of the balanced augmented matrix

Row weights of the balanced augmented matrix.

Formalized by `StatMech.Onsager.ons_decMiddleBalancedRowWeight`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationMiddleBalanced.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationMiddleBalanced.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-middle-balanced-row-weight).

## Column weights of the balanced augmented matrix

Column weights of the balanced augmented matrix.

Formalized by `StatMech.Onsager.ons_decMiddleBalancedColWeight`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationMiddleBalanced.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationMiddleBalanced.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-middle-balanced-col-weight).

## Reversal on augmented states

Reversal on augmented states: reverse darts and swap the two sides.

Formalized by `StatMech.Onsager.ons_decMiddleAugRev`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationMiddleCancellation.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationMiddleCancellation.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-middle-aug-rev).

## Directions of augmented states

Directions of augmented states: the direction of a dart, and east or west for the two sides.

Formalized by `StatMech.Onsager.ons_decMiddleAugDir`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationMiddleCancellation.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationMiddleCancellation.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-middle-aug-dir).

## Row weights of the augmented Kac-Ward matrix

Row weights of the augmented matrix: `1` on darts and `t` times the middle weight on side
states.

Formalized by `StatMech.Onsager.ons_decMiddleRowWeight`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationMiddleCancellation.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationMiddleCancellation.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-middle-row-weight).

## Column weights of the augmented Kac-Ward matrix

Column weights of the augmented matrix: the external weight on darts and `1` on side states.

Formalized by `StatMech.Onsager.ons_decMiddleColWeight`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationMiddleCancellation.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationMiddleCancellation.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-middle-col-weight).

## Reversal-invariant internal factor of the augmented matrix

The reversal-invariant internal factor of the augmented matrix.

Formalized by `StatMech.Onsager.ons_decMiddleInternalFactor`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationMiddleCancellation.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationMiddleCancellation.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-middle-internal-factor).

## Test for a dart traversing an external edge

Whether a dart of the decorated graph traverses an external edge (from a torus dart to its
reverse).

Formalized by `StatMech.Onsager.ons_decDartIsExternal`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationWalkExtract.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationWalkExtract.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-dart-is-external).

## External darts of a decorated walk in order

The torus darts at which a decorated walk traverses an external edge, in order.

Formalized by `StatMech.Onsager.ons_decWalkExternalDarts`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationWalkExtract.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationWalkExtract.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-walk-external-darts).

## First-return loop of a rooted decorated cycle

The first-return loop at `d` read off from a decorated cycle rooted at `d`: the root, the
remaining external darts in reverse order, and the root again.

Formalized by `StatMech.Onsager.ons_decCycleFirstReturn`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationWalkExtract.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationWalkExtract.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-cycle-first-return).

## Adjacency of directions along the port line

Two directions are adjacent in the order `0, 1, 2, 3` of the internal path at a site.

Formalized by `StatMech.Onsager.ons_portLineAdj`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationTurnTransfer.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationTurnTransfer.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-port-line-adj).

## Micro directions along internal decorated edges at a site

The micro directions of the routes along a sequence of internal decorated edges at one site.

Formalized by `StatMech.Onsager.ons_internalMicroDirections`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationTurnTransfer.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationTurnTransfer.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-internal-micro-directions).

## Directions of the expanded dart list of a decorated walk

The directions of the expanded dart list of a decorated walk.

Formalized by `StatMech.Onsager.ons_walkExpandedDirections`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationTurnTransfer.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationTurnTransfer.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-walk-expanded-directions).

## Directions of the external darts of a decorated walk

The directions of the external darts of a decorated walk.

Formalized by `StatMech.Onsager.ons_walkExternalDirections`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationTurnTransfer.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationTurnTransfer.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-walk-external-directions).

## Internal walk between two ports at a site

A walk along the internal path from port `a` to port `b` at a site.

Formalized by `StatMech.Onsager.ons_decPortChainWalk`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationTransitionWalk.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationTransitionWalk.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-port-chain-walk).

## Internal path between two ports at a site

The internal path from port `a` to port `b` at a site, as a path in the decorated graph.

Formalized by `StatMech.Onsager.ons_decPortChainPath`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationTransitionWalk.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationTransitionWalk.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-port-chain-path).

## Decorated walk of a Kac-Ward transition

The decorated walk of the Kac-Ward transition from `d₁` to `d₂`: the external edge at `d₁`
followed by the internal path to `d₂`.

Formalized by `StatMech.Onsager.ons_decTransitionWalk`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationTransitionWalk.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationTransitionWalk.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-transition-walk).

## Head-to-tail relation between darts

Dart `target` starts at the head of dart `source`.

Formalized by `StatMech.Onsager.ons_decGeometricStep`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationLoopWalk.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationLoopWalk.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-geometric-step).

## Edge multiset of a decorated walk as an exponent

The multiset of edges of a decorated walk, as an exponent.

Formalized by `StatMech.Onsager.ons_decWalkEdgeCount`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationLoopWalk.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationLoopWalk.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-walk-edge-count).

## Transition exponent sum along a dart chain

The sum of the transition exponents along a chain of darts starting at `start`.

Formalized by `StatMech.Onsager.ons_decKWChainExponent`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationLoopWalk.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationLoopWalk.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-kwchain-exponent).

## Last dart of a dart chain

The last dart of a chain starting at `start`.

Formalized by `StatMech.Onsager.ons_decKWChainLast`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationLoopWalk.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationLoopWalk.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-kwchain-last).

## Decorated walk of a chain of darts

The decorated walk obtained by concatenating the trails of the transitions along a chain of
darts.

Formalized by `StatMech.Onsager.ons_decWalkOfKWChain`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationLoopWalk.lean, line 301](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationLoopWalk.lean#L301). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-walk-of-kwchain).

## Darts of a Kac-Ward loop in walking order

The darts of a Kac-Ward loop in walking order (reversed indexing).

Formalized by `StatMech.Onsager.ons_decGeometricLoopStates`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationLoopWalk.lean, line 457](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationLoopWalk.lean#L457). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-geometric-loop-states).

## Closed decorated walk of a valid Kac-Ward loop

The closed decorated walk of a valid closed Kac-Ward walk, rooted at its first dart.

Formalized by `StatMech.Onsager.ons_decLoopWalk`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationLoopWalk.lean, line 529](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationLoopWalk.lean#L529). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-loop-walk).

## Dart list of a rooted decorated cycle

The first-return loop of a rooted decorated cycle without its final repeated dart.

Formalized by `StatMech.Onsager.ons_decCycleDartList`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationWalkHomology.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationWalkHomology.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-cycle-dart-list).

## Closed dart walk of a rooted decorated cycle

The closed walk of darts of a rooted decorated cycle, indexed by `Fin` of its length.

Formalized by `StatMech.Onsager.ons_decCycleDartLoop`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationWalkHomology.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationWalkHomology.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-dec-cycle-dart-loop).

## Simple graph spanned by an edge set

The simple graph on `V` whose edges are the non-loop elements of `F`; this is
`SimpleGraph.fromEdgeSet F`.

Formalized by `StatMech.Onsager.ons_edgeSubgraph`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TrivalentCycles.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TrivalentCycles.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html#ons-edge-subgraph).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Trivalent decoration of the torus](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/exact-solutions/trivalent-decoration-of-the-torus)
