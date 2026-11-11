---
declaration: section
origin: cited
lean: StatMech.Sharpness.RandomCurrent.aie_allConn, StatMech.Sharpness.RandomCurrent.aie_noneConn, StatMech.Sharpness.RandomCurrent.aie_mass, StatMech.Sharpness.RandomCurrent.aie_gap, StatMech.Sharpness.RandomCurrent.ahd_triEnds, StatMech.Sharpness.RandomCurrent.ahd_hdom_refutable, StatMech.Sharpness.RandomCurrent.asd_ghsBackboneFactor, StatMech.Ising.atb_backbone
statement: formalized
proof: formalized
---

# Griffiths–Hurst–Sherman inequality

96 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html).

## Current connecting all three site pairs

The current `m` connects each of the pairs `{x, y}`, `{o, y}`, `{o, x}`.

Formalized by `StatMech.Sharpness.RandomCurrent.aie_allConn`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/AizenmanInclusionExclusion.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/AizenmanInclusionExclusion.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#aie-all-conn).

## Current connecting none of the three site pairs

The current `m` connects none of the pairs `{x, y}`, `{o, y}`, `{o, x}`.

Formalized by `StatMech.Sharpness.RandomCurrent.aie_noneConn`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/AizenmanInclusionExclusion.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/AizenmanInclusionExclusion.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#aie-none-conn).

## Mass of sub-currents with a given source set

The total weight `∑ φ(K)` of the sub-currents `K ⊆ m` with source set `S`.

Formalized by `StatMech.Sharpness.RandomCurrent.aie_mass`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/AizenmanInclusionExclusion.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/AizenmanInclusionExclusion.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#aie-mass).

## GHS gap of a sourced current

The GHS gap `mass(A) - mass(A ∆ {x, y}) - mass(A ∆ {o, y}) - mass(A ∆ {o, x})`.

Formalized by `StatMech.Sharpness.RandomCurrent.aie_gap`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/AizenmanInclusionExclusion.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/AizenmanInclusionExclusion.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#aie-gap).

## Edges of the triangle on three vertices

The three edges `{0, 1}`, `{1, 2}`, `{0, 2}` of the triangle on `Fin 3`.

Formalized by `StatMech.Sharpness.RandomCurrent.ahd_triEnds`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/AizenmanHdom.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/AizenmanHdom.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ahd-tri-ends).

## Domination condition fails on the triangle

The domination condition fails for the single current through all edges of the triangle.

Formalized by `StatMech.Sharpness.RandomCurrent.ahd_hdom_refutable`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/AizenmanHdom.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/AizenmanHdom.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ahd-hdom-refutable).

## Three-site backbone factor

The three-site backbone factor: `1`, `0` or `-2` according to how many of the pairs `{x, y},
{o, y}, {o, x}` the current connects.

Formalized by `StatMech.Sharpness.RandomCurrent.asd_ghsBackboneFactor`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/AizenmanSignDominance.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/AizenmanSignDominance.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#asd-ghs-backbone-factor).

## Backbone cluster of a site in a current

The cluster of `o` in the current `m`: the sites connected to `o` by edges of `m`.

Formalized by `StatMech.Ising.atb_backbone`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/AizenmanTrueBackbone.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/AizenmanTrueBackbone.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#atb-backbone).

## Conditioned domination condition over a set of currents

The domination condition `2 · mass(all connected) ≤ mass(none connected)`, summed over
currents in `M`.

Formalized by `StatMech.Ising.atb_conditionedDom`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/AizenmanTrueBackbone.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/AizenmanTrueBackbone.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#atb-conditioned-dom).

## Three-site duplicated-variable factor

The three-site duplicated-variable factor `1 - σ_x σ_y - σ_o σ_y - σ_o σ_x` of the configuration
`q`.

Formalized by `StatMech.Ising.ghsQFactor`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSDistinctSite.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSDistinctSite.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghs-qfactor).

## Three-replica Ising expectation

The expectation of `F a b c` over three independent copies `a, b, c` of the Ising Gibbs
distribution.

Formalized by `StatMech.Ising.isingExp3`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSDuplicateVariable.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSDuplicateVariable.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ising-exp3).

## Three-replica variable $d_w$

The three-replica variable `d_w = σ_w(b) + σ_w(c) - 2σ_w(a)`.

Formalized by `StatMech.Ising.dvar`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSDuplicateVariable.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSDuplicateVariable.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#dvar).

## Two-replica Ising expectation

The expectation of `F a b` over two independent copies `a, b` of the Ising Gibbs
distribution.

Formalized by `StatMech.Ising.isingExp2`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSDuplicateVariable.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSDuplicateVariable.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ising-exp2).

## Rotated two-replica difference variable $u_w$

The rotated two-replica variable `u_w = (σ_w(a) - σ_w(b)) / 2`.

Formalized by `StatMech.Ising.uvar`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSDuplicateVariable.lean, line 328](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSDuplicateVariable.lean#L328). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#uvar).

## Rotated two-replica sum variable $t_w$

The rotated two-replica variable `t_w = (σ_w(a) + σ_w(b)) / 2`.

Formalized by `StatMech.Ising.tvar`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSDuplicateVariable.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSDuplicateVariable.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#tvar).

## Edges of the induced subgraph on a vertex set

The edges of `E` with both endpoints in `S` (the edges of the induced subgraph on `S`).

Formalized by `StatMech.Ising.ghsvp_vertexEdges`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSVertexPartition.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSVertexPartition.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghsvp-vertex-edges).

## Zero-field partition function of an induced subgraph

The zero-field partition function of the induced subgraph on `S`, with couplings `J`.

Formalized by `StatMech.Ising.ghsvp_vertexZ`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSVertexPartition.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSVertexPartition.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghsvp-vertex-z).

## Zero-field correlation in an induced subgraph

The zero-field correlation `⟨σ_P⟩` in the induced subgraph on `S`.

Formalized by `StatMech.Ising.ghsvp_vertexCorr`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSVertexPartition.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSVertexPartition.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghsvp-vertex-corr).

## Correlation with field in an induced subgraph

The correlation `⟨σ_P⟩` in the induced subgraph on `S`, with field `hf`.

Formalized by `StatMech.Ising.ghsvp_vertexCorrField`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSVertexPartition.lean, line 264](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSVertexPartition.lean#L264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghsvp-vertex-corr-field).

## Configuration merged from two configurations along a set

The configuration equal to `a` on `S` and to `b` off `S`.

Formalized by `StatMech.Ising.ghsvp_mergeConfig`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSVertexPartition.lean, line 305](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSVertexPartition.lean#L305). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghsvp-merge-config).

## Splitting a configuration into a set and its complement

Configurations split into their restrictions to `S` and to its complement.

Formalized by `StatMech.Ising.ghsvp_splitConfig`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSVertexPartition.lean, line 310](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSVertexPartition.lean#L310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghsvp-split-config).

## Induced-subgraph partition function over the active sites only

The partition function of the induced subgraph on `S`, summed over configurations on `S`
only.

Formalized by `StatMech.Ising.ghsvp_activeZ`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSVertexPartition.lean, line 348](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSVertexPartition.lean#L348). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghsvp-active-z).

## Image of a vertex set among non-ghost vertices

The image of `A` among the non-ghost vertices `some x` of `Option V`.

Formalized by `StatMech.Ising.ghsvp_someSet`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSVertexPartition.lean, line 377](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSVertexPartition.lean#L377). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghsvp-some-set).

## Image of a vertex set together with the ghost vertex

The image of `A` together with the ghost vertex `none`.

Formalized by `StatMech.Ising.ghsvp_fieldSet`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSVertexPartition.lean, line 380](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSVertexPartition.lean#L380). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghsvp-field-set).

## Weight of an agreement set in the duplicated system

The weight of the agreement set `A` in the duplicated system: the product of the ghost-vertex
partition functions of `A ∪ {ghost}` and of `Aᶜ`, with doubled couplings `2β` and field
`2βh`.

Formalized by `StatMech.Ising.ghsvp_subsetMass`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSVertexPartition.lean, line 385](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSVertexPartition.lean#L385). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghsvp-subset-mass).

## Induced-subgraph partition function with doubled coupling and field

The partition function on the induced subgraph on `A` with couplings `2β` and field `2βh`.

Formalized by `StatMech.Ising.ghsvp_tZ`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSVertexPartition.lean, line 589](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSVertexPartition.lean#L589). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghsvp-t-z).

## Zero-field induced-subgraph partition function with doubled coupling

The zero-field partition function on the induced subgraph on `A` with couplings `2β`.

Formalized by `StatMech.Ising.ghsvp_uZ`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSVertexPartition.lean, line 595](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSVertexPartition.lean#L595). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghsvp-u-z).

## Two-point correlation on the disagreement subgraph

The zero-field correlation `⟨σ_o σ_x⟩` in the subgraph induced by `Aᶜ` (couplings `2β`), or
`0` if `o` or `x` lies in `A`.

Formalized by `StatMech.Ising.ghsvp_disagreementCorr`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSVertexPartition.lean, line 716](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSVertexPartition.lean#L716). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghsvp-disagreement-corr).

## Magnetization on the agreement subgraph

The magnetization `⟨σ_y⟩` in the subgraph induced by `A` (couplings `2β`, field `2βh`), or
`0` if `y ∉ A`.

Formalized by `StatMech.Ising.ghsvp_agreementMag`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSVertexPartition.lean, line 723](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSVertexPartition.lean#L723). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghsvp-agreement-mag).

## Inhomogeneous ghost-vertex couplings

The ghost-vertex couplings: `2K_{xy}` on an edge `{x, y}`, `2h_x` between `x` and the ghost.

Formalized by `StatMech.Ising.ghsiGhostCoupling`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSInhomVertexPartition.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSInhomVertexPartition.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghsi-ghost-coupling).

## Inhomogeneous induced-subgraph partition function with field

The partition function of the subgraph induced by `A` with couplings `2K` and fields `2h` on
`A`.

Formalized by `StatMech.Ising.ghsiTZ`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSInhomVertexPartition.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSInhomVertexPartition.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghsi-tz).

## Inhomogeneous zero-field induced-subgraph partition function

The zero-field partition function of the subgraph induced by `A` with couplings `2K`.

Formalized by `StatMech.Ising.ghsiUZ`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSInhomVertexPartition.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSInhomVertexPartition.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghsi-uz).

## Inhomogeneous weight of an agreement set

The weight of the agreement set `A` in the duplicated inhomogeneous system.

Formalized by `StatMech.Ising.ghsiSubsetMass`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSInhomVertexPartition.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSInhomVertexPartition.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghsi-subset-mass).

## Total spin of a configuration

The total spin `∑_x σ_x` of a configuration.

Formalized by `StatMech.Sharpness.totalSpin`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MagnetizationFieldDeriv.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MagnetizationFieldDeriv.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#total-spin).

## Griffiths' second inequality for two distinct spins

Griffiths' second inequality for two distinct spins: `⟨σ_x⟩⟨σ_y⟩ ≤ ⟨σ_x σ_y⟩` for `β, h ≥ 0`.

Formalized by `StatMech.Sharpness.cov_nonneg`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MagnetizationFieldDeriv.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MagnetizationFieldDeriv.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#cov-nonneg).

## Field derivative of the magnetization as a sum of covariances

The field derivative of the magnetization is `β` times the sum of the two-point covariances
`⟨σ_o σ_x⟩ - ⟨σ_o⟩⟨σ_x⟩` (the finite-volume susceptibility).

Formalized by `StatMech.Sharpness.deriv_magnetization_eq_sum_cov`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MagnetizationFieldDeriv.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MagnetizationFieldDeriv.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#deriv-magnetization-eq-sum-cov).

## Global spin flip

The global spin flip `σ ↦ -σ`.

Formalized by `StatMech.Sharpness.flipCfg`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MagnetizationFieldDeriv.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MagnetizationFieldDeriv.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#flip-cfg).

## Global spin flip as an involutive equivalence

The global spin flip as an involutive equivalence of configuration space.

Formalized by `StatMech.Sharpness.flipEquiv`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MagnetizationFieldDeriv.lean, line 292](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MagnetizationFieldDeriv.lean#L292). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#flip-equiv).

## Magnetization vanishes at zero field

At zero field the global spin-flip symmetry forces the magnetization `⟨σ_o⟩_{β,0}` to vanish.

Formalized by `StatMech.Sharpness.magnetization_zero_field`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MagnetizationFieldDeriv.lean, line 299](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MagnetizationFieldDeriv.lean#L299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#magnetization-zero-field).

## Susceptibility bound $\chi(h) \le m(h)/h \le 1/h$ from concavity

If the magnetization is concave in the field on `[0, ∞)` (the GHS inequality), then for `h > 0`
the susceptibility satisfies `χ(h) ≤ m(h)/h ≤ 1/h`. Reference: R. B. Griffiths, C. A. Hurst, S.
Sherman, "Concavity of magnetization of an Ising ferromagnet in a positive external field", J. Math.
Phys. 11 (1970) 790–795.

Formalized by `StatMech.Sharpness.ghs_susceptibility_bound`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MagnetizationFieldDeriv.lean, line 325](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MagnetizationFieldDeriv.lean#L325). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghs-susceptibility-bound).

## Agreement configuration of two spin configurations

The agreement configuration of `a` and `b`: `true` exactly at the sites where they agree.

Formalized by `StatMech.Ising.ghsLAgreement`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghs-lagreement).

## Mate of a configuration over an agreement pattern

The configuration that agrees with `a` where `q` is `true` and disagrees where `q` is
`false`.

Formalized by `StatMech.Ising.ghsLMate`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghs-lmate).

## Set of sites where an agreement configuration is true

The set of sites where `q` is `true`.

Formalized by `StatMech.Ising.ghsLAgreeFinset`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghs-lagree-finset).

## Agreement-set Boltzmann weight with doubled couplings and field

The Boltzmann weight, with couplings `2β` and field `2βh`, of `a` on the subgraph induced by
the agreement set of `q`.

Formalized by `StatMech.Ising.ghsLTWeight`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghs-ltweight).

## Zero-field disagreement-set Boltzmann weight

The zero-field Boltzmann weight, with couplings `2β`, of `a` on the subgraph induced by the
disagreement set of `q`.

Formalized by `StatMech.Ising.ghsLUWeight`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghs-luweight).

## Splitting a configuration along the agreement set

Configurations split into their restrictions to the agreement and disagreement sets of `q`.

Formalized by `StatMech.Ising.ghsLSplitEquiv`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghs-lsplit-equiv).

## Completion of agreement-set spins to a full configuration

The configuration with given spins on the agreement set of `q` and `false` elsewhere.

Formalized by `StatMech.Ising.ghsLTComplete`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghs-ltcomplete).

## Completion of disagreement-set spins to a full configuration

The configuration with given spins on the disagreement set of `q` and `false` elsewhere.

Formalized by `StatMech.Ising.ghsLUComplete`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean, line 325](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean#L325). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghs-lucomplete).

## Change of variables from replica pairs to agreement and first copy

The change of variables `(a, b) ↦ (agreement of a and b, a)` on pairs of configurations.

Formalized by `StatMech.Ising.ghsLXnorEquiv`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean, line 420](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean#L420). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghs-lxnor-equiv).

## Two-replica weight in an agreement fibre

The two-replica weight of `a` and its mate in the fibre over the agreement configuration `q`.

Formalized by `StatMech.Ising.ghsLFibreWeight`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean, line 448](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean#L448). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghs-lfibre-weight).

## Total two-replica weight of an agreement fibre

The total two-replica weight of the fibre over `q`.

Formalized by `StatMech.Ising.ghsLFibreMass`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean, line 452](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean#L452). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghs-lfibre-mass).

## Fibre weight integrated against an observable

The two-replica weight of the fibre over `q`, integrated against `F`.

Formalized by `StatMech.Ising.ghsLFibreNumerator`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean, line 456](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean#L456). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghs-lfibre-numerator).

## Conditional two-replica expectation given the agreement

The conditional two-replica expectation of `F` given the agreement configuration `q`.

Formalized by `StatMech.Ising.ghsLFibreExpectation`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean, line 462](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean#L462). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghs-lfibre-expectation).

## Law of the agreement configuration of two replicas

The probability that two independent replicas have agreement configuration `q`.

Formalized by `StatMech.Ising.ghsLAgreementProb`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean, line 467](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean#L467). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghs-lagreement-prob).

## Conditional expectation of $u_o u_x$ given the agreement

The conditional expectation `E[u_o u_x | q]` of the rotated variables.

Formalized by `StatMech.Ising.ghsLFibreUU`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean, line 663](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean#L663). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghs-lfibre-uu).

## Conditional expectation of $t_y$ given the agreement

The conditional expectation `E[t_y | q]` of the rotated variable.

Formalized by `StatMech.Ising.ghsLFibreT`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean, line 667](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean#L667). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghs-lfibre-t).

## Zero-field expectation on the disagreement set

The zero-field expectation on the subgraph induced by the disagreement set of `q`.

Formalized by `StatMech.Ising.ghsLUExpectation`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean, line 671](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean#L671). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghs-luexpectation).

## Expectation with field on the agreement set

The expectation with field on the subgraph induced by the agreement set of `q`.

Formalized by `StatMech.Ising.ghsLTExpectation`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean, line 677](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean#L677). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghs-ltexpectation).

## Field weight of the disagreement set

The field weight `exp (2βh ∑_{v ∉ q} σ_v(a))` of the disagreement set.

Formalized by `StatMech.Ising.ghsLOutFieldWeight`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean, line 837](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean#L837). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghs-lout-field-weight).

## Fibre factorization property for $u_o u_x$ and $t_y$

Conditioned on the agreement configuration, `u_o u_x` and `t_y` are uncorrelated.

Formalized by `StatMech.Ising.GHSLebowitzFibreFactorization`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean, line 957](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean#L957). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghslebowitz-fibre-factorization).

## FKG lattice condition for the agreement law when $\beta, h \ge 0$

The law of the agreement configuration satisfies the FKG lattice condition.

Formalized by `StatMech.Ising.ghsLAgreementProb_fkg`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean, line 1091](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean#L1091). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghs-lagreement-prob-fkg).

## Griffiths–Hurst–Sherman inequality

For the ferromagnetic Ising model on a finite graph
with `β ≥ 0` and `h ≥ 0`, the third Ursell function `u₃(o, x, y)` is nonpositive for every
site `o` and every edge `{x, y}`.

R. B. Griffiths, C. A. Hurst and S. Sherman, *Concavity of magnetization of an Ising
ferromagnet in a positive external field*, J. Math. Phys. 11 (1970); proof of J. L. Lebowitz,
*GHS and other inequalities*, Comm. Math. Phys. 35 (1974).

Formalized by `StatMech.Ising.ghsL_threePoint`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean, line 1122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSLebowitz.lean#L1122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghs-l-three-point).

## Derivative of a concave function is at most a secant slope

The derivative of a concave function on `[0, ∞)` at `b` is at most the secant slope over `[a,
b]`. This is Mathlib's `ConcaveOn.deriv_le_slope` with the slope unfolded.

Formalized by `StatMech.Sharpness.shg_concaveOn_deriv_le_slope`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/GHSConcavity.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/GHSConcavity.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#shg-concave-on-deriv-le-slope).

## Concavity from a nonpositive second derivative on $(0, \infty)$

A continuous function on `[0, ∞)`, twice differentiable on the interior with nonpositive second
derivative, is concave. This is Mathlib's `concaveOn_of_deriv2_nonpos` specialized to `Ici 0`.

Formalized by `StatMech.Sharpness.shg_concaveOn_of_deriv2_nonpos`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/GHSConcavity.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/GHSConcavity.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#shg-concave-on-of-deriv2-nonpos).

## Susceptibility bound $\chi(h) \le m(h)/h$ from concavity

If the magnetization is concave in the field on `[0, ∞)`, then for `h > 0` the susceptibility
satisfies `χ(h) ≤ m(h)/h`, using `m(0) = 0`.

Formalized by `StatMech.Sharpness.shg_magnetization_susceptibility_bound`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/GHSConcavity.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/GHSConcavity.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#shg-magnetization-susceptibility-bound).

## Two-replica expectation with inhomogeneous couplings

The expectation of `F a b` over two independent copies of the Ising model with couplings `K`
and fields `hf`.

Formalized by `StatMech.Ising.ghsiExp2`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghsi-exp2).

## Inhomogeneous agreement-set Boltzmann weight

The Boltzmann weight, with couplings `2K` and fields `2hf`, of `a` on the subgraph induced by
the agreement set of `q`.

Formalized by `StatMech.Ising.ghsiTWeight`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghsi-tweight).

## Inhomogeneous zero-field disagreement-set weight

The zero-field Boltzmann weight, with couplings `2K`, of `a` on the subgraph induced by the
disagreement set of `q`.

Formalized by `StatMech.Ising.ghsiUWeight`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghsi-uweight).

## Inhomogeneous two-replica weight in an agreement fibre

The two-replica weight of `a` and its mate in the fibre over the agreement configuration `q`.

Formalized by `StatMech.Ising.ghsiFibreWeight`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean, line 371](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean#L371). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghsi-fibre-weight).

## Inhomogeneous total weight of an agreement fibre

The total two-replica weight of the fibre over `q`.

Formalized by `StatMech.Ising.ghsiFibreMass`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean, line 376](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean#L376). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghsi-fibre-mass).

## Inhomogeneous fibre weight integrated against an observable

The two-replica weight of the fibre over `q`, integrated against `F`.

Formalized by `StatMech.Ising.ghsiFibreNumerator`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean, line 381](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean#L381). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghsi-fibre-numerator).

## Inhomogeneous conditional expectation given the agreement

The conditional two-replica expectation of `F` given the agreement configuration `q`.

Formalized by `StatMech.Ising.ghsiFibreExpectation`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean, line 386](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean#L386). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghsi-fibre-expectation).

## Inhomogeneous law of the agreement configuration

The probability that two independent replicas have agreement configuration `q`.

Formalized by `StatMech.Ising.ghsiAgreementProb`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean, line 391](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean#L391). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghsi-agreement-prob).

## Inhomogeneous conditional expectation of $u_o u_x$

The conditional expectation `E[u_o u_x | q]` of the rotated variables.

Formalized by `StatMech.Ising.ghsiFibreUU`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean, line 498](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean#L498). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghsi-fibre-uu).

## Inhomogeneous conditional expectation of $t_y$

The conditional expectation `E[t_y | q]` of the rotated variable.

Formalized by `StatMech.Ising.ghsiFibreT`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean, line 503](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean#L503). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghsi-fibre-t).

## Inhomogeneous zero-field expectation on the disagreement set

The zero-field expectation on the subgraph induced by the disagreement set of `q`.

Formalized by `StatMech.Ising.ghsiUExpectation`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean, line 508](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean#L508). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghsi-uexpectation).

## Inhomogeneous expectation with field on the agreement set

The expectation with field on the subgraph induced by the agreement set of `q`.

Formalized by `StatMech.Ising.ghsiTExpectation`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean, line 514](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean#L514). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghsi-texpectation).

## Inhomogeneous two-point correlation on the disagreement set

The zero-field correlation `⟨σ_o σ_x⟩` on the subgraph induced by `Aᶜ` (couplings `2K`), or
`0` if `o` or `x` lies in `A`.

Formalized by `StatMech.Ising.ghsiDisagreementCorr`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean, line 643](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean#L643). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghsi-disagreement-corr).

## Inhomogeneous magnetization on the agreement set

The magnetization `⟨σ_y⟩` on the subgraph induced by `A` (couplings `2K`, fields `2hf`), or
`0` if `y ∉ A`.

Formalized by `StatMech.Ising.ghsiAgreementMag`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean, line 650](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean#L650). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghsi-agreement-mag).

## Inhomogeneous field weight of the disagreement set

The field weight `exp (∑_{v ∉ q} 2h_v σ_v(a))` of the disagreement set.

Formalized by `StatMech.Ising.ghsiOutFieldWeight`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean, line 735](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean#L735). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghsi-out-field-weight).

## Griffiths–Hurst–Sherman inequality

**Griffiths–Hurst–Sherman inequality** for inhomogeneous ferromagnets. With couplings `K_e ≥
0` and fields `h_x ≥ 0`, the third Ursell function satisfies `u₃(o, x, y) ≤ 0` whenever `o ≠
x`.

R. B. Griffiths, C. A. Hurst and S. Sherman, *Concavity of magnetization of an Ising
ferromagnet in a positive external field*, J. Math. Phys. 11 (1970); J. L. Lebowitz, *GHS and
other inequalities*, Comm. Math. Phys. 35 (1974).

Formalized by `StatMech.Ising.ghsi_ursell_nonpos`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean, line 1085](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean#L1085). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghsi-ursell-nonpos).

## Directional spin sum

The directional spin `∑_x d_x σ_x`.

Formalized by `StatMech.Ising.ghsiDirSpin`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean, line 1105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean#L1105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghsi-dir-spin).

## Field line in a given direction

The field line `t ↦ h + t·d`.

Formalized by `StatMech.Ising.ghsiFieldLine`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean, line 1109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean#L1109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghsi-field-line).

## Covariance with the directional spin

The covariance of `f` with the directional spin `∑_x d_x σ_x`.

Formalized by `StatMech.Ising.ghsiDirectionalCovariance`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean, line 1205](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean#L1205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghsi-directional-covariance).

## Third Ursell function of the inhomogeneous Ising model

The third Ursell function `u₃(o, x, y)` of the inhomogeneous Ising model.

Formalized by `StatMech.Ising.ghsiUrsell3`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean, line 1238](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean#L1238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghsi-ursell3).

## Third Ursell function nonpositive for $o \ne x$, $K, h \ge 0$

The GHS inequality `u₃(o, x, y) ≤ 0` for the named Ursell function, when `o ≠ x`.

Formalized by `StatMech.Ising.ghsiUrsell3_nonpos`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean, line 1252](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean#L1252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghsi-ursell3-nonpos).

## Spin covariance in the inhomogeneous model

The spin covariance `⟨σ_o σ_x⟩ - ⟨σ_o⟩⟨σ_x⟩`.

Formalized by `StatMech.Ising.ghsiCovariance`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean, line 1335](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean#L1335). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghsi-covariance).

## GHS concavity

With couplings `K_e ≥ 0`, fields `h_x ≥ 0`, and a direction `d ≥ 0` with
`d_o = 0`, the magnetization `⟨σ_o⟩` is concave in `t ≥ 0` along the field line `h + t·d`.

R. B. Griffiths, C. A. Hurst and S. Sherman, J. Math. Phys. 11 (1970).

Formalized by `StatMech.Ising.ghsi_magnetization_fieldLine_concaveOn`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean, line 1450](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GHSInhomogeneous.lean#L1450). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghsi-magnetization-field-line-concave-on).

## Field derivative of the two-point covariance

The field derivative of the two-point covariance `Cov(σ_o, σ_x)`, written as a combination of
Gibbs expectations involving the total spin.

Formalized by `StatMech.Walls.gc4_D1cov2`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MagnetizationConcavity.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MagnetizationConcavity.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#gc4-d1cov2).

## Third Ursell function of the finite Ising model

The third Ursell function (joint cumulant) `u₃(o, x, y) = ⟨σ_oσ_xσ_y⟩ - ⟨σ_o⟩⟨σ_xσ_y⟩ -
⟨σ_oσ_x⟩⟨σ_y⟩ - ⟨σ_oσ_y⟩⟨σ_x⟩ + 2⟨σ_o⟩⟨σ_x⟩⟨σ_y⟩` of the finite Ising model at `(β, h)`.

Formalized by `StatMech.Walls.GhcEqGap.eg_ursell3`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/UrsellGap.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/UrsellGap.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#eg-ursell3).

## GHS gap on an edge equals the third Ursell function

On an edge `{x, y}`, the gap `cov3sym - ghsBoundSym` between the three-point covariance and the
GHS bound equals `u₃(o, x, y)`.

Formalized by `StatMech.Walls.GhcEqGap.ghc_ursellEqGap`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/UrsellGap.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/UrsellGap.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghc-ursell-eq-gap).

## Lebowitz four-point combination

Lebowitz's four-point combination `⟨σ_oσ_xσ_y⟩ - ⟨σ_oσ_x⟩⟨σ_y⟩ - ⟨σ_oσ_y⟩⟨σ_x⟩ - ⟨σ_o⟩⟨σ_xσ_y⟩`,
which differs from the Ursell function `u₃` by `2⟨σ_o⟩⟨σ_x⟩⟨σ_y⟩`.

Formalized by `StatMech.Walls.gc_lebowitzU4`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/GHSSignCondition.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/GHSSignCondition.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#gc-lebowitz-u4).

## GHS sign condition

The GHS sign condition at `(β, h)` and root `o`: the third Ursell function `u₃(o, x, y)` is
nonpositive for all pairwise distinct `o, x, y`. It holds for `β, h ≥ 0` by `ghs_signDominance`.

Formalized by `StatMech.Walls.GHSSignDominance`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/GHSSignCondition.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/GHSSignCondition.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghssign-dominance).

## Griffiths–Hurst–Sherman inequality

The Griffiths–Hurst–Sherman inequality: for `β ≥ 0` and `h ≥ 0`, the third Ursell function
`u₃(o, x, y)` is nonpositive for distinct sites. Reference: R. B. Griffiths, C. A. Hurst, S.
Sherman, "Concavity of magnetization of an Ising ferromagnet in a positive external field", J. Math.
Phys. 11 (1970) 790–795; proof via J. L. Lebowitz, "GHS and other inequalities", Comm. Math. Phys.
35 (1974) 87–92.

Formalized by `StatMech.Sharpness.ghs_signDominance`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/GHSInequality.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/GHSInequality.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghs-sign-dominance).

## GHS concavity of the magnetization in the field

GHS concavity: for `β ≥ 0` the magnetization `h ↦ ⟨σ_o⟩_{β,h}` is concave on `[0, ∞)`.
Reference: R. B. Griffiths, C. A. Hurst, S. Sherman, "Concavity of magnetization of an Ising
ferromagnet in a positive external field", J. Math. Phys. 11 (1970) 790–795.

Formalized by `StatMech.Sharpness.ghs_magnetization_concaveOn`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/GHSInequality.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/GHSInequality.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghs-magnetization-concave-on).

## GHS susceptibility bound $\chi \le 1/h$

The GHS susceptibility bound: for `β ≥ 0` and `h > 0`, the field derivative of the magnetization
equals `β ∑_x (⟨σ_oσ_x⟩ - ⟨σ_o⟩⟨σ_x⟩)` and is at most `1/h`. Reference: R. B. Griffiths, C. A.
Hurst, S. Sherman, "Concavity of magnetization of an Ising ferromagnet in a positive external
field", J. Math. Phys. 11 (1970) 790–795. Scope: a finite graph with uniform coupling and uniform
field, the field entering the Hamiltonian as `-h ∑ σ_x` and the derivative taken in `h`; `χ ≤ 1/h`
is the weak form of the GHS consequence `χ ≤ m/h`, the full concavity statement being
`ghs_magnetization_concaveOn`. The hypotheses `β ≥ 0`, `h > 0` are satisfiable.

Formalized by `StatMech.Sharpness.ghs_susceptibility_le_inv_field`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/GHSInequality.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/GHSInequality.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html#ghs-susceptibility-le-inv-field).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Griffiths–Hurst–Sherman inequality](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-hurst-sherman-inequality)
