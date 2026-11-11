---
declaration: section
origin: cited
lean: StatMech.Sharpness.abcrEndpointSum, StatMech.Sharpness.abcrIncidentCoupling, StatMech.Sharpness.edgeWeightV, StatMech.Sharpness.configWeightV, StatMech.Sharpness.weightOffV, StatMech.Sharpness.probV, StatMech.Sharpness.pivotalProbV, StatMech.Sharpness.paramOn
statement: formalized
proof: formalized
---

# Aizenman–Barsky inequality

50 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html).

## Endpoint sum on unordered pairs

The function `s(x, y) ↦ F(x) + F(y)` on unordered pairs.

Formalized by `StatMech.Sharpness.abcrEndpointSum`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABCouplingReindex.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABCouplingReindex.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#abcr-endpoint-sum).

## Incident coupling of a vertex

The incident coupling `∑_{y ∼ x} J_{xy}` of `x`, as a sum over darts starting at `x`.

Formalized by `StatMech.Sharpness.abcrIncidentCoupling`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABCouplingReindex.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABCouplingReindex.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#abcr-incident-coupling).

## Edge weight under an inhomogeneous product measure

The probability `p_e` or `1 - p_e` of the state of edge `e` in `ω`.

Formalized by `StatMech.Sharpness.edgeWeightV`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABFieldDeriv.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABFieldDeriv.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#edge-weight-v).

## Product weight of a configuration

The product weight `∏_e (p_e or 1 - p_e)` of a configuration.

Formalized by `StatMech.Sharpness.configWeightV`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABFieldDeriv.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABFieldDeriv.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#config-weight-v).

## Product weight of a configuration off one edge

The product weight of a configuration over all edges other than `e`.

Formalized by `StatMech.Sharpness.weightOffV`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABFieldDeriv.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABFieldDeriv.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#weight-off-v).

## Probability under an inhomogeneous product measure

The probability `∑_ω 1_A(ω) ∏_e (p_e or 1 - p_e)` of `A` under the inhomogeneous product
measure.

Formalized by `StatMech.Sharpness.probV`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABFieldDeriv.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABFieldDeriv.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#prob-v).

## Pivotal probability of an edge

The probability that `e` is pivotal for `A`.

Formalized by `StatMech.Sharpness.pivotalProbV`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABFieldDeriv.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABFieldDeriv.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#pivotal-prob-v).

## Edge parameters set to a common value on a subset

The parameters `p` with the value `c` on the edges of `s`.

Formalized by `StatMech.Sharpness.paramOn`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABFieldDeriv.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABFieldDeriv.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#param-on).

## Ghost-edge probability $1 - e^{-h}$

The ghost-edge probability `1 - e^{-h}`.

Formalized by `StatMech.Sharpness.qField`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABFieldDeriv.lean, line 363](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABFieldDeriv.lean#L363). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#q-field).

## Extension of a vertex permutation to the ghost graph

The extension of a vertex permutation to the ghost graph fixing the ghost.

Formalized by `StatMech.Sharpness.abfsOptionEquiv`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABFiniteSymmetry.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABFiniteSymmetry.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#abfs-option-equiv).

## Induced permutation of ghost-graph edges

The induced permutation of unordered pairs of the ghost graph.

Formalized by `StatMech.Sharpness.abfsEdgeEquiv`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABFiniteSymmetry.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABFiniteSymmetry.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#abfs-edge-equiv).

## Configurations with an edge closed and pivotal

Configurations in which `e` is closed and pivotal for `A`.

Formalized by `StatMech.Sharpness.abgiClosedPivotal`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABGhostInfluence.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABGhostInfluence.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#abgi-closed-pivotal).

## Edge parameters with a field value on a subset

Edge parameters `1 - e^{-βJ_e}` off `s` and `q` on `s`.

Formalized by `StatMech.Sharpness.abpdBetaFieldParams`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABPhysicalDeriv.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABPhysicalDeriv.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#abpd-beta-field-params).

## Edges used by an open walk in an induced subgraph

The edges of `V` used by a walk in the open subgraph induced on `A`.

Formalized by `StatMech.Sharpness.sab_inducedEdgeSet`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABPivotalFirstExit.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABPivotalFirstExit.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#sab-induced-edge-set).

## Transfer of an open walk between agreeing configurations

An open walk in `A` for `ω`, read as an open walk for `ω'` when `ω` and `ω'` agree on its edges.

Formalized by `StatMech.Sharpness.sab_inducedWalkTransfer`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABPivotalFirstExit.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABPivotalFirstExit.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#sab-induced-walk-transfer).

## Transfer of an open walk avoiding a fixed edge

An open walk for `ω_S` avoiding the edge `xy`, read as an open walk for `ω` when the two agree
off `xy`.

Formalized by `StatMech.Sharpness.sab_transfer_avoid`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABPivotalFirstExit.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABPivotalFirstExit.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#sab-transfer-avoid).

## Coupling restricted to the edges of a graph

The coupling `J` restricted to the edges of `G`.

Formalized by `StatMech.Sharpness.abfaBaseCoupling`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABFiniteGraph.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABFiniteGraph.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#abfa-base-coupling).

## Coupling lifted to the ghost graph

The coupling on the ghost graph: `J` on the edges of `G` and `0` on the ghost edges.

Formalized by `StatMech.Sharpness.abfaLiftCoupling`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABFiniteGraph.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABFiniteGraph.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#abfa-lift-coupling).

## Edge parameters with a ghost field

Edge parameters `1 - e^{-βJ_e}` on the edges of `G` and `1 - e^{-h}` on the ghost edges.

Formalized by `StatMech.Sharpness.abfaParams`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABFiniteGraph.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABFiniteGraph.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#abfa-params).

## Finite-volume percolation magnetization

The percolation magnetization `M(β, h) = P(o ↔ ghost)`.

Formalized by `StatMech.Sharpness.abfaMag`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABFiniteGraph.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABFiniteGraph.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#abfa-mag).

## Aizenman–Barsky inequality on a finite graph

The Aizenman–Barsky inequality on a finite graph: if all row sums equal `J₀` and all sites have
the same magnetization, then `∂_β M ≤ J₀ M ∂_h M` for `β, h ≥ 0`. Reference: M. Aizenman, D. J.
Barsky, "Sharpness of the phase transition in percolation models", Comm. Math. Phys. 108 (1987)
489–526.

Formalized by `StatMech.Sharpness.abfa_aizenmanBarsky`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABFiniteGraph.lean, line 383](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABFiniteGraph.lean#L383). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#abfa-aizenman-barsky).

## Merging configurations on and off a set

The configuration equal to `γ` on `s` and to `η` off `s`.

Formalized by `StatMech.Sharpness.abgrMerge`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABGhostRegularity.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABGhostRegularity.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#abgr-merge).

## Closing all ghost edges but one

Close all ghost edges except `{x, ghost}`.

Formalized by `StatMech.Sharpness.abgrKeepGhost`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABGhostRegularity.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABGhostRegularity.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#abgr-keep-ghost).

## Closing all ghost edges

Close all ghost edges.

Formalized by `StatMech.Sharpness.abgrCloseGhost`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABGhostRegularity.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABGhostRegularity.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#abgr-close-ghost).

## Sites connected to $o$ with ghost edges closed

The sites connected to `o` when all ghost edges are closed.

Formalized by `StatMech.Sharpness.abgrActive`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABGhostRegularity.lean, line 343](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABGhostRegularity.lean#L343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#abgr-active).

## Correspondence between sites and ghost edges

Sites correspond to ghost edges.

Formalized by `StatMech.Sharpness.abgrGhostEdgeEquiv`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABGhostRegularity.lean, line 361](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABGhostRegularity.lean#L361). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#abgr-ghost-edge-equiv).

## Ghost edges at the physical cluster of $o$

The ghost edges at sites of the cluster of `o` in the physical configuration `η`.

Formalized by `StatMech.Sharpness.abgrActiveGhost`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABGhostRegularity.lean, line 404](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABGhostRegularity.lean#L404). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#abgr-active-ghost).

## Probability of a physical configuration

The probability of the physical configuration `η`.

Formalized by `StatMech.Sharpness.abgrOffWeight`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABGhostRegularity.lean, line 477](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABGhostRegularity.lean#L477). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#abgr-off-weight).

## Aizenman–Barsky inequality for all $\beta$ and $h$

The Aizenman–Barsky inequality `∂_β M(β, h) ≤ J M(β, h) ∂_h M(β, h)` for all `β, h`.

Formalized by `StatMech.Sharpness.AizenmanBarskyInequality`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/AizenmanBarsky.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/AizenmanBarsky.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#aizenman-barsky-inequality).

## Second Aizenman–Barsky inequality

The second Aizenman–Barsky inequality `M ≤ h ∂_h M + M² + β M ∂_β M`.

Formalized by `StatMech.Sharpness.AizenmanBarskyPDI`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/AizenmanBarsky.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/AizenmanBarsky.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#aizenman-barsky-pdi).

## Aizenman–Barsky critical bound $M(\beta_c, h) \ge c\sqrt{h}$

The Aizenman–Barsky critical bound: from `∂_β M ≤ J M ∂_h M` and `1 - M(β_c, h) ≤ β_c ∂_β M(β_c,
h)` with `M(β_c, 0) = 0`, `M(β_c, h) ≥ c √h` for `0 < h ≤ β_c J/4`. Reference: M. Aizenman, D. J.
Barsky, "Sharpness of the phase transition in percolation models", Comm. Math. Phys. 108 (1987)
489–526.

Formalized by `StatMech.Sharpness.ab_perco_meanfield_sqrt`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/AizenmanBarsky.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/AizenmanBarsky.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#ab-perco-meanfield-sqrt).

## Aizenman–Barsky inequality for $\beta \ge 0$ and $h > 0$

The Aizenman–Barsky inequality `∂_β M ≤ J M ∂_h M` for `β ≥ 0` and `h > 0`.

Formalized by `StatMech.Sharpness.AizenmanBarskyInequalityPhysical`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/AizenmanBarsky.lean, line 321](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/AizenmanBarsky.lean#L321). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#aizenman-barsky-inequality-physical).

## Real edge parameters with a ghost field

The real edge parameters: `1 - e^{-βJ_e}` on physical edges and `1 - e^{-h}` on ghost edges.

Formalized by `StatMech.Sharpness.abigRealParam`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABInfiniteGhost.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABInfiniteGhost.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#abig-real-param).

## Edge parameters as nonnegative reals

The edge parameters as elements of `ℝ≥0`.

Formalized by `StatMech.Sharpness.abigParam`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABInfiniteGhost.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABInfiniteGhost.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#abig-param).

## Bond percolation measure on the ghost graph

Independent bond percolation on the ghost graph with parameters `abigParam`.

Formalized by `StatMech.Sharpness.abigMeasure`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABInfiniteGhost.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABInfiniteGhost.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#abig-measure).

## Infinite-volume percolation magnetization

The percolation magnetization `M(β, h) = P(o ↔ ghost)`.

Formalized by `StatMech.Sharpness.abigMag`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABInfiniteGhost.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABInfiniteGhost.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#abig-mag).

## Internal edges of a finite set

The unordered pairs with both endpoints in `T`.

Formalized by `StatMech.Sharpness.abigInternalEdges`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABInfiniteGhost.lean, line 292](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABInfiniteGhost.lean#L292). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#abig-internal-edges).

## Unordered pairs of a set as its internal edges

Unordered pairs of `T` correspond to `abigInternalEdges T`.

Formalized by `StatMech.Sharpness.abigInternalEdgeEquiv`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABInfiniteGhost.lean, line 307](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABInfiniteGhost.lean#L307). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#abig-internal-edge-equiv).

## Ghost window of a finite set

The window `S ∪ {ghost}` in the ghost graph.

Formalized by `StatMech.Sharpness.abigGhostWindow`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABInfiniteGhost.lean, line 335](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABInfiniteGhost.lean#L335). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#abig-ghost-window).

## Ghost window as a set with one added point

`Option S` corresponds to the window `S ∪ {ghost}`.

Formalized by `StatMech.Sharpness.abigGhostWindowEquiv`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABInfiniteGhost.lean, line 340](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABInfiniteGhost.lean#L340). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#abig-ghost-window-equiv).

## Unordered pairs of the extended set as window edges

Unordered pairs of `Option S` correspond to the internal edges of the window.

Formalized by `StatMech.Sharpness.abigWindowEdgeEquiv`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABInfiniteGhost.lean, line 364](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABInfiniteGhost.lean#L364). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#abig-window-edge-equiv).

## Subgraph induced on a window

The subgraph of `G` induced on `S`.

Formalized by `StatMech.Sharpness.abigWindowGraph`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABInfiniteGhost.lean, line 377](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABInfiniteGhost.lean#L377). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#abig-window-graph).

## Coupling restricted to a window

The coupling restricted to the window.

Formalized by `StatMech.Sharpness.abigWindowCoupling`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABInfiniteGhost.lean, line 388](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABInfiniteGhost.lean#L388). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#abig-window-coupling).

## Darts at a vertex as its neighbours

Darts starting at `x` correspond to neighbours of `x`.

Formalized by `StatMech.Sharpness.abigDartFiberEquivNeighbor`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABInfiniteGhost.lean, line 398](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABInfiniteGhost.lean#L398). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#abig-dart-fiber-equiv-neighbor).

## Uniform row-sum bound in finite windows

All row sums of `J` in all finite windows are at most `J₀`.

Formalized by `StatMech.Sharpness.abigUniformFiniteRowBound`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABInfiniteGhost.lean, line 438](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABInfiniteGhost.lean#L438). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#abig-uniform-finite-row-bound).

## Largest site magnetization in a window

The largest site magnetization in the window.

Formalized by `StatMech.Sharpness.abigWindowEnvelope`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABInfiniteGhost.lean, line 860](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABInfiniteGhost.lean#L860). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#abig-window-envelope).

## Aizenman–Barsky inequality on infinite vertex-transitive graphs

The Aizenman–Barsky inequality on infinite vertex-transitive graphs with translation-invariant
couplings supported on edges and row sums at most `J₀`: `∂_β M ≤ J₀ M ∂_h M` for `β ≥ 0`, `h > 0`.
Reference: M. Aizenman, D. J. Barsky, "Sharpness of the phase transition in percolation models",
Comm. Math. Phys. 108 (1987) 489–526.

Formalized by `StatMech.Sharpness.abig_aizenmanBarskyPhysical_of_tsum_transitive`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABInfiniteGhost.lean, line 1633](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABInfiniteGhost.lean#L1633). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#abig-aizenman-barsky-physical-of-tsum-tr).

## Box as a finite set of sites

The box `Λ_n` as a finite set of sites.

Formalized by `StatMech.Sharpness.ablBoxFinset`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABHypercubic.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABHypercubic.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#abl-box-finset).

## Aizenman–Barsky inequality on $\mathbb{Z}^d$ with neighbour row sum

The Aizenman–Barsky inequality on `ℤ^d` with the row sum written over lattice neighbours.
Reference: M. Aizenman, D. J. Barsky, "Sharpness of the phase transition in percolation models",
Comm. Math. Phys. 108 (1987) 489–526. Scope and fidelity: this is the first Aizenman–Barsky
differential inequality `∂_β M ≤ |J| M ∂_h M` for independent bond percolation on `ℤ^d` with
nearest-neighbour, translation-invariant couplings `J ≥ 0` (edge probability `1 - e^{-βJ_e}`) and a
ghost field (ghost-edge probability `1 - e^{-h}`), for `β ≥ 0`, `h > 0`; `M(β, h)` is the
probability that the origin is connected to the ghost. Aizenman–Barsky allow general summable
translation-invariant couplings; here `J` vanishes off lattice edges. A derivative is taken to be $0$ where the function is not differentiable: `M` is differentiable in `h`, and at a point where `β ↦ M(β, h)` is not differentiable the inequality holds trivially.

Formalized by `StatMech.Sharpness.abl_aizenmanBarsky_hypercubic_neighbourSum`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABHypercubic.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABHypercubic.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#abl-aizenman-barsky-hypercubic-neighbour).

## Aizenman–Barsky inequality on $\mathbb{Z}^d$

The Aizenman–Barsky inequality on `ℤ^d`: `∂_β M ≤ |J| M ∂_h M` with `|J| = ∑_y J_{0y}`.
Reference: M. Aizenman, D. J. Barsky, "Sharpness of the phase transition in percolation models",
Comm. Math. Phys. 108 (1987) 489–526. Scope and fidelity: this is the first Aizenman–Barsky
differential inequality `∂_β M ≤ |J| M ∂_h M` for independent bond percolation on `ℤ^d` with
nearest-neighbour, translation-invariant couplings `J ≥ 0` (edge probability `1 - e^{-βJ_e}`) and a
ghost field (ghost-edge probability `1 - e^{-h}`), for `β ≥ 0`, `h > 0`; `M(β, h)` is the
probability that the origin is connected to the ghost. Aizenman–Barsky allow general summable
translation-invariant couplings; here `J` vanishes off lattice edges. A derivative is taken to be $0$ where the function is not differentiable: `M` is differentiable in `h`, and at a point where `β ↦ M(β, h)` is not differentiable the inequality holds trivially.

Formalized by `StatMech.Sharpness.abl_aizenmanBarsky_hypercubic`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABHypercubic.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ABHypercubic.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html#abl-aizenman-barsky-hypercubic).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Aizenman–Barsky inequality](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/percolation/sharpness/aizenman-barsky-inequality)
