---
declaration: section
origin: cited
lean: StatMech.FK.fbd_offCentreCarrier, StatMech.FK.fk_unique_of_edgeMarg_eq, StatMech.FK.countable_edgeMarg_ne, StatMech.FK.phi0_eq_phi1_off_countable, StatMech.FK.countable_phi_ne, StatMech.FK.fkEdgeOpenEvent, StatMech.FK.wiredEdgeDensity, StatMech.FK.freeEdgeDensity
statement: formalized
proof: formalized
---

# Per-box agreement of free and wired random-cluster measures

100 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html).

## Wired-marginal difference between a box and its translate

The difference between the wired marginal of `eb'` on `Λ_{N+k}` and on the translate of
`Λ_{N+k}` by `v`, evaluated at the translated edge.

Formalized by `StatMech.FK.fbd_offCentreCarrier`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoundaryInfluenceDecay.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/BoundaryInfluenceDecay.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#fbd-off-centre-carrier).

## Monotone-coupled laws with equal edge marginals agree on up-sets

Two monotonically coupled probability vectors with equal edge marginals agree on increasing
events. Restatement of `eventMass_eq_of_edgeMarg_eq` (`EdgeMarginal`), kept because other modules
use this name.

Formalized by `StatMech.FK.fk_unique_of_edgeMarg_eq`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/Uniqueness.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/Uniqueness.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#fk-unique-of-edge-marg-eq).

## Agreement with a monotone map at continuity points fails countably

If `a` agrees with a monotone `b` at every continuity point of `b`, then `{p | a p ≠ b p}` is
countable.

Formalized by `StatMech.FK.countable_edgeMarg_ne`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/Uniqueness.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/Uniqueness.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#countable-edge-marg-ne).

## Parametric agreement on increasing events off a countable set

Parametric agreement: if for each `p` there is a monotone coupling of `μ p` and `ν p`, and edge
marginals agree at every continuity point of the monotone map `p ↦ ν_p(ω(e) = 1)`, then `μ p` and `ν
p` agree on increasing events for all `p` outside a countable set.

Formalized by `StatMech.FK.phi0_eq_phi1_off_countable`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/Uniqueness.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/Uniqueness.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#phi0-eq-phi1-off-countable).

## Countably many parameters admit a separating increasing event

Under the hypotheses of `phi0_eq_phi1_off_countable`, the set of `p` for which some increasing
event separates `μ p` and `ν p` is countable.

Formalized by `StatMech.FK.countable_phi_ne`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/Uniqueness.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/Uniqueness.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#countable-phi-ne).

## Event that an edge is open

The event that the edge `e` is open.

Formalized by `StatMech.FK.fkEdgeOpenEvent`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/UniquenessOffCountable.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/UniquenessOffCountable.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#fk-edge-open-event).

## Wired infinite-volume edge density

The edge density `φ^1_{p,q}(e open)` of the wired infinite-volume random-cluster measure on
`ℤ^d`, set to `0` outside `p ∈ (0, 1)`, `q > 0`.

Formalized by `StatMech.FK.wiredEdgeDensity`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/UniquenessOffCountable.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/UniquenessOffCountable.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#wired-edge-density).

## Free infinite-volume edge density

The edge density `φ^0_{p,q}(e open)` of the free infinite-volume random-cluster measure on
`ℤ^d`, set to `0` outside `p ∈ (0, 1)`, `q > 0`.

Formalized by `StatMech.FK.freeEdgeDensity`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/UniquenessOffCountable.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/UniquenessOffCountable.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#free-edge-density).

## Wired–free gap in the $q = 2$ density of a box edge

The gap `φ^1_{p,2}(eb open) - φ^0_{p,2}(eb open)` between the wired and free infinite-volume
densities of the edge `eb` of `Λ_N`.

Formalized by `StatMech.FK.docGap`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/DecayOfCorrelations.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/DecayOfCorrelations.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#doc-gap).

## Shell edge fraction is at most $4d^2(n-m)/n$

The fraction of ordered edges of `Λ_n` outside `Λ_m` is at most `4 d² (n - m)/n`.

Formalized by `StatMech.FK.ocs_edgeCard_shell_fraction_le`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreSandwich.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreSandwich.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ocs-edge-card-shell-fraction-le).

## Vanishing shell edge fraction when $(n - m(n))/n \to 0$

If `(n - m(n))/n → 0`, the edges of `Λ_n` outside `Λ_{m(n)}` form a vanishing fraction of
the edges of `Λ_n`.

Formalized by `StatMech.FK.ocs_edgeFinset_shell_fraction_tendsto_zero`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreSandwich.lean, line 300](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreSandwich.lean#L300). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ocs-edge-finset-shell-fraction-tendsto-z).

## Free off-centre lower bound by the recentred small-box marginal

For `u, v` adjacent in `Λ_{n-R}`, the free marginal in `Λ_n` of the edge `{u, v}` is at least
the free marginal in `Λ_R` of the recentered edge `{0, v - u}`.

Formalized by `StatMech.FK.ocs_free_offCentre_lower`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreSandwich.lean, line 357](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreSandwich.lean#L357). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ocs-free-off-centre-lower).

## Wired off-centre upper bound by the recentred small-box marginal

For `u, v` adjacent in `Λ_{n-R-1}` and `R ≥ 1`, the wired marginal in `Λ_n` of `{u, v}` is at
most the wired marginal in `Λ_R` of the recentered edge `{0, v - u}`.

Formalized by `StatMech.FK.ocs_wired_offCentre_upper`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreSandwich.lean, line 416](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreSandwich.lean#L416). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ocs-wired-off-centre-upper).

## Adjacent box vertices differ by a signed unit vector

The difference of adjacent box vertices is a signed unit vector. See also `rot_edge_dir`.

Formalized by `StatMech.FK.ocs_edge_dir_candMap`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreSandwich.lean, line 475](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreSandwich.lean#L475). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ocs-edge-dir-cand-map).

## Unit edge $\{0, \pm e_j\}$ of a box

The unit edge `{0, ±e_j}` of the box `Λ_R`, `R ≥ 1`, indexed by `(j, sign)`.

Formalized by `StatMech.FK.ocs_unitEdge`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreSandwich.lean, line 493](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreSandwich.lean#L493). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ocs-unit-edge).

## Free unit-edge marginals converge to the free density

The free marginal of a unit edge in `Λ_{⌊√n⌋}` converges to its free `q = 2` density.

Formalized by `StatMech.FK.ocs_unitEdge_marg_tendsto`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreSandwich.lean, line 514](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreSandwich.lean#L514). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ocs-unit-edge-marg-tendsto).

## Free rotation residue for a box pair

The free rotation residue at tilt `t` for the box pair `e'`: every lattice edge of every box
has the free `q = 2` density of `e'` at `p = logistic t`.

Formalized by `StatMech.FK.ocs_FreeRotationResidue`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreSandwich.lean, line 548](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreSandwich.lean#L548). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ocs-free-rotation-residue).

## Free unit-edge marginal in the square-root box

The free marginal at `p = logistic t` of the unit edge `(j, sign)` in `Λ_{⌊√n⌋}`, and `0`
when `⌊√n⌋ = 0`.

Formalized by `StatMech.FK.ocs_unitMarg`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreSandwich.lean, line 555](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreSandwich.lean#L555). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ocs-unit-marg).

## Total deviation of free unit-edge marginals from the density

The total deviation `∑_{(j, sign)} |density(e') - unit-edge marginal|` of the free unit-edge
marginals in `Λ_{⌊√n⌋}` from the free density of `e'`.

Formalized by `StatMech.FK.ocs_freeDelta`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreSandwich.lean, line 563](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreSandwich.lean#L563). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ocs-free-delta).

## Bulk edges of $\Lambda_n$

The bulk edges of `Λ_n`: the edges of the inner box `Λ_{n - ⌊√n⌋}`.

Formalized by `StatMech.FK.ocs_bulkSet`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreSandwich.lean, line 611](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreSandwich.lean#L611). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ocs-bulk-set).

## Lower bound on free bulk edge marginals

Every bulk edge of `Λ_n` has free marginal at least `density(e') - ocs_freeDelta`.

Formalized by `StatMech.FK.ocs_free_bulk_lower`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreSandwich.lean, line 615](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreSandwich.lean#L615). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ocs-free-bulk-lower).

## Free off-centre sandwich from free rotation residues

The free off-centre sandwich from the free rotation residues for all pairs `e'` of `Λ_N`.

Formalized by `StatMech.FK.ocs_freeOffCentreSandwich_of_rotation`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreSandwich.lean, line 654](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreSandwich.lean#L654). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ocs-free-off-centre-sandwich-of-rotation).

## Wired unit-edge marginals converge to the wired density

The wired marginal of a unit edge in `Λ_{⌊√n⌋}` converges to its wired `q = 2` density.

Formalized by `StatMech.FK.ocs_unitEdge_wired_marg_tendsto`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreSandwich.lean, line 711](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreSandwich.lean#L711). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ocs-unit-edge-wired-marg-tendsto).

## Wired rotation residue for a box pair

The wired rotation residue at tilt `t` for the box pair `e'`: every lattice edge of every box
has the wired `q = 2` density of `e'` at `p = logistic t`.

Formalized by `StatMech.FK.ocs_WiredRotationResidue`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreSandwich.lean, line 743](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreSandwich.lean#L743). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ocs-wired-rotation-residue).

## Wired unit-edge marginal in the square-root box

The wired marginal at `p = logistic t` of the unit edge `(j, sign)` in `Λ_{⌊√n⌋}`, and `0`
when `⌊√n⌋ = 0`.

Formalized by `StatMech.FK.ocs_unitWiredMarg`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreSandwich.lean, line 750](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreSandwich.lean#L750). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ocs-unit-wired-marg).

## Total deviation of wired unit-edge marginals from the density

The total deviation of the wired unit-edge marginals in `Λ_{⌊√n⌋}` from the wired density of
`e'`.

Formalized by `StatMech.FK.ocs_wiredDelta`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreSandwich.lean, line 759](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreSandwich.lean#L759). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ocs-wired-delta).

## Wired bulk edges of $\Lambda_n$

The wired bulk edges of `Λ_n`: the edges of the inner box `Λ_{n - ⌊√n⌋ - 1}`.

Formalized by `StatMech.FK.ocs_wiredBulkSet`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreSandwich.lean, line 797](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreSandwich.lean#L797). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ocs-wired-bulk-set).

## Upper bound on wired bulk edge marginals

Every wired bulk edge of `Λ_n` has wired marginal at most `density(e') + ocs_wiredDelta`.

Formalized by `StatMech.FK.ocs_wired_bulk_upper`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreSandwich.lean, line 802](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreSandwich.lean#L802). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ocs-wired-bulk-upper).

## Wired off-centre sandwich from wired rotation residues

The wired off-centre sandwich from the wired rotation residues for all pairs `e'` of
`Λ_N`.

Formalized by `StatMech.FK.ocs_wiredOffCentreSandwich_of_rotation`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreSandwich.lean, line 849](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreSandwich.lean#L849). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ocs-wired-off-centre-sandwich-of-rotatio).

## Free $q = 2$ bulk sandwich from equal free edge densities

If every free `q = 2` edge density equals that of `e'`, then each box `Λ_n` has a bulk set of
edges with that density whose free marginals are at least the density minus `δ_n → 0`, and the
non-bulk edge fraction tends to zero.

Formalized by `StatMech.FK.gec_freeSandwich_of_rotation`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/GenuineEdgeCollapse.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/GenuineEdgeCollapse.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#gec-free-sandwich-of-rotation).

## Wired $q = 2$ bulk sandwich from equal wired edge densities

If every wired `q = 2` edge density equals that of `e'`, then each box `Λ_n` has a bulk set of
edges with that density whose wired marginals are at most the density plus `δ_n → 0`, and the
non-bulk edge fraction tends to zero.

Formalized by `StatMech.FK.gec_wiredSandwich_of_rotation`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/GenuineEdgeCollapse.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/GenuineEdgeCollapse.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#gec-wired-sandwich-of-rotation).

## Two-sided free $q = 2$ bulk bounds from the free sandwich

The free sandwich gives two-sided bulk bounds: free marginals within `δ_n` of the density,
since free marginals increase to the density.

Formalized by `StatMech.FK.gec_freeBulk_of_sandwich`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/GenuineEdgeCollapse.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/GenuineEdgeCollapse.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#gec-free-bulk-of-sandwich).

## Two-sided wired $q = 2$ bulk bounds from the wired sandwich

The wired sandwich gives two-sided bulk bounds: wired marginals within `δ_n` of the density,
since wired marginals decrease to the density.

Formalized by `StatMech.FK.gec_wiredBulk_of_sandwich`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/GenuineEdgeCollapse.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/GenuineEdgeCollapse.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#gec-wired-bulk-of-sandwich).

## Coordinate permutation of $\mathbb{Z}^d$

The permutation of `ℤ^d` permuting coordinates by `π`: `(x ∘ π⁻¹)_i = x_{π⁻¹ i}`.

Formalized by `StatMech.FK.rot_permEquiv`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/RotationInvariance.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/RotationInvariance.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#rot-perm-equiv).

## Coordinate permutation as a box symmetry

A coordinate permutation as a box symmetry.

Formalized by `StatMech.FK.rot_permBoxSym`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/RotationInvariance.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/RotationInvariance.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#rot-perm-box-sym).

## Box symmetries preserve the free $q = 2$ density of any pair of sites

Box symmetries preserve the free `q = 2` density of any edge of `ℤ^d`.

Formalized by `StatMech.FK.rot_free_density_boxSym`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/RotationInvariance.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/RotationInvariance.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#rot-free-density-box-sym).

## Box symmetries preserve the wired $q = 2$ density of any pair of sites

Box symmetries preserve the wired `q = 2` density of any edge of `ℤ^d`.

Formalized by `StatMech.FK.rot_wired_density_boxSym`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/RotationInvariance.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/RotationInvariance.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#rot-wired-density-box-sym).

## Reference edge $\{0, e_0\}$ of $\mathbb{Z}^d$

The reference edge `{0, e_0}` of `ℤ^d`.

Formalized by `StatMech.FK.rot_refUnitEdge`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/RotationInvariance.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/RotationInvariance.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#rot-ref-unit-edge).

## Unit edges at the origin have the free density of $\{0, e_0\}$

Every unit edge `{0, ±e_j}` has the free density of `{0, e_0}`.

Formalized by `StatMech.FK.rot_free_centred_unit_const`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/RotationInvariance.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/RotationInvariance.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#rot-free-centred-unit-const).

## Unit edges at the origin have the wired density of $\{0, e_0\}$

Every unit edge `{0, ±e_j}` has the wired density of `{0, e_0}`.

Formalized by `StatMech.FK.rot_wired_centred_unit_const`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/RotationInvariance.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/RotationInvariance.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#rot-wired-centred-unit-const).

## Adjacent sites differ by a signed unit vector

The difference of adjacent sites is a signed unit vector. See also `ocs_edge_dir_candMap`,
the same statement for vertices of a box.

Formalized by `StatMech.FK.rot_edge_dir`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/RotationInvariance.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/RotationInvariance.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#rot-edge-dir).

## Every lattice edge has the free $q = 2$ density of $\{0, e_0\}$

Every nearest-neighbour edge of `ℤ^d` has the free `q = 2` density of `{0, e_0}`.

Formalized by `StatMech.FK.rot_free_edge_const`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/RotationInvariance.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/RotationInvariance.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#rot-free-edge-const).

## Every lattice edge has the wired $q = 2$ density of $\{0, e_0\}$

Every nearest-neighbour edge of `ℤ^d` has the wired `q = 2` density of `{0, e_0}`.

Formalized by `StatMech.FK.rot_wired_edge_const`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/RotationInvariance.lean, line 302](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/RotationInvariance.lean#L302). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#rot-wired-edge-const).

## All box edges have the same free $q = 2$ density

The free rotation residue holds for every lattice edge `e'` of the box `Λ_N`.

Formalized by `StatMech.FK.rot_freeRotationResidue`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/RotationInvariance.lean, line 335](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/RotationInvariance.lean#L335). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#rot-free-rotation-residue).

## All box edges have the same wired $q = 2$ density

The wired rotation residue holds for every lattice edge `e'` of the box `Λ_N`.

Formalized by `StatMech.FK.rot_wiredRotationResidue`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/RotationInvariance.lean, line 343](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/RotationInvariance.lean#L343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#rot-wired-rotation-residue).

## Free growing-box collapse at $q = 2$

Free growing-box collapse: for every edge `e'` of `Λ_N` and every `t`, the average free edge
density of `Λ_n` converges to the free infinite-volume density of `e'`.

Formalized by `StatMech.FK.ubd_FreeGrowingBoxCollapse`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/UniformBulkDeviation.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/UniformBulkDeviation.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ubd-free-growing-box-collapse).

## Free $q = 2$ edge density lies in $(0, 1)$

The free infinite-volume `q = 2` edge density lies in `[0, 1]`.

Formalized by `StatMech.FK.ubd_freeEdgeDensity_mem_Icc`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/UniformBulkDeviation.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/UniformBulkDeviation.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ubd-free-edge-density-mem-icc).

## Nonnegativity of wired FK edge marginals

Edge marginals of a wired FK measure are nonnegative.

Formalized by `StatMech.FK.ubd_edgeMargProb_wiredFkProb_nonneg`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/UniformBulkDeviation.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/UniformBulkDeviation.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ubd-edge-marg-prob-wired-fk-prob-nonneg).

## Wired FK edge marginals are at most one

Edge marginals of a wired FK measure are at most `1`.

Formalized by `StatMech.FK.ubd_edgeMargProb_wiredFkProb_le_one`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/UniformBulkDeviation.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/UniformBulkDeviation.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ubd-edge-marg-prob-wired-fk-prob-le-one).

## Wired $q = 2$ edge density lies in $(0, 1)$

The wired infinite-volume `q = 2` edge density lies in `[0, 1]`.

Formalized by `StatMech.FK.ubd_wiredEdgeDensity_mem_Icc`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/UniformBulkDeviation.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/UniformBulkDeviation.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ubd-wired-edge-density-mem-icc).

## Average wired $q = 2$ edge density of a box as a mean of marginals

The average wired edge density of `Λ_n` is the mean of the wired edge marginals.

Formalized by `StatMech.FK.ubd_avgWiredDensity_eq_sum`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/UniformBulkDeviation.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/UniformBulkDeviation.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ubd-avg-wired-density-eq-sum).

## Free uniform bulk deviation at $q = 2$

Free uniform bulk deviation: for every edge `e'` and `t`, each box `Λ_n` has a bulk edge set
with free marginals within `δ_n → 0` of the free density of `e'`, and the non-bulk edge
fraction tends to zero.

Formalized by `StatMech.FK.ubd_FreeUniformBulkDeviation`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/UniformBulkDeviation.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/UniformBulkDeviation.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ubd-free-uniform-bulk-deviation).

## Wired uniform bulk deviation at $q = 2$

Wired uniform bulk deviation: for every edge `e'` and `t`, each box `Λ_n` has a bulk edge set
with wired marginals within `δ_n → 0` of the wired density of `e'`, and the non-bulk edge
fraction tends to zero.

Formalized by `StatMech.FK.ubd_WiredUniformBulkDeviation`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/UniformBulkDeviation.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/UniformBulkDeviation.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ubd-wired-uniform-bulk-deviation).

## Free $q = 2$ infinite-volume mass function on a box

The mass function on configurations of `Λ_N` of the free `q = 2` infinite-volume measure at
`p = logistic(t)`, restricted to `Λ_N`.

Formalized by `StatMech.FK.fuc_freeMass`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/UniquenessFromFreeEnergy.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/UniquenessFromFreeEnergy.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#fuc-free-mass).

## Wired $q = 2$ infinite-volume mass function on a box

The mass function on configurations of `Λ_N` of the wired `q = 2` infinite-volume measure at
`p = logistic(t)`, restricted to `Λ_N`.

Formalized by `StatMech.FK.fuc_wiredMass`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/UniquenessFromFreeEnergy.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/UniquenessFromFreeEnergy.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#fuc-wired-mass).

## Homogeneous free-energy data on a box at $q = 2$

There is a convex `g` whose right and left derivatives at `t` are the wired and free `q = 2`
edge
densities at `p = logistic(t)`, for every edge of `Λ_N`.

Formalized by `StatMech.FK.fuc_HomogeneousFreeEnergyData`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/UniquenessFromFreeEnergy.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/UniquenessFromFreeEnergy.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#fuc-homogeneous-free-energy-data).

## Free-energy data give $q = 2$ box uniqueness off countably many $t$

Given `fuc_HomogeneousFreeEnergyData`, the free and wired `q = 2` measures agree on every
increasing event of `Λ_N` for all but countably many `t`.

Formalized by `StatMech.FK.fuc_fk_uniqueness`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/UniquenessFromFreeEnergy.lean, line 298](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/UniquenessFromFreeEnergy.lean#L298). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#fuc-fk-uniqueness).

## Toggle-invariant coordinates are open with probability one half

A coordinate whose toggle preserves a probability mass function is open with probability `1/2`.

Formalized by `StatMech.FK.fpe2_edgeMargProb_half_of_toggle_invariant`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FKUniqPerEdge.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FKUniqPerEdge.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#fpe2-edge-marg-prob-half-of-toggle-invar).

## Per-coordinate free energy on a box

The per-coordinate free energy on `Λ_N`: `G` on edges of the box graph and `s ↦ s/2` on
non-edges.

Formalized by `StatMech.FK.fpe2_perEdgeG`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FKUniqPerEdge.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FKUniqPerEdge.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#fpe2-per-edge-g).

## Free densities of genuine box edges as left derivatives

Every edge of `Λ_N` has free `q = 2` density at `p = logistic(t)` equal to the left derivative
`G'₋(t)`.

Formalized by `StatMech.FK.fpe2_GenuineFreeIsLeftDeriv`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FKUniqPerEdge.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FKUniqPerEdge.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#fpe2-genuine-free-is-left-deriv).

## Wired densities of genuine box edges as right derivatives

Every edge of `Λ_N` has wired `q = 2` density at `p = logistic(t)` equal to the right
derivative
`G'₊(t)`.

Formalized by `StatMech.FK.fpe2_GenuineWiredIsRightDeriv`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FKUniqPerEdge.lean, line 289](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FKUniqPerEdge.lean#L289). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#fpe2-genuine-wired-is-right-deriv).

## Countable-exception $q = 2$ uniqueness from one-sided derivative data

If the free and wired densities of the edges of `Λ_N` are the left and right derivatives of one
convex `G`, the free and wired `q = 2` measures agree on increasing events of `Λ_N` for all but
countably many `t`.

Formalized by `StatMech.FK.fpe2_fk_uniqueness_of_genuine`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FKUniqPerEdge.lean, line 354](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FKUniqPerEdge.lean#L354). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#fpe2-fk-uniqueness-of-genuine).

## Free average edge density collapse on boxes

The average free edge density of `Λ_n` converges to the free infinite-volume density of every
edge
of `Λ_N`.

Formalized by `StatMech.FK.fpe2_GenuineFreeCollapse`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FKUniqPerEdge.lean, line 375](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FKUniqPerEdge.lean#L375). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#fpe2-genuine-free-collapse).

## Wired average edge density collapse on boxes

The average wired edge density of `Λ_n` converges to the wired infinite-volume density of every
edge of `Λ_N`.

Formalized by `StatMech.FK.fpe2_GenuineWiredCollapse`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FKUniqPerEdge.lean, line 383](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FKUniqPerEdge.lean#L383). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#fpe2-genuine-wired-collapse).

## Configurations closed off the edges of a graph

Configurations closed on every coordinate that is not an edge of `G`.

Formalized by `StatMech.FK.ecz_ClosedOff`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ecz-closed-off).

## Edge partition function of the random-cluster model

The edge partition function: the sum of FK weights over configurations closed off `E(G)`.

Formalized by `StatMech.FK.ecz_fkZEdge`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ecz-fk-zedge).

## Number of non-edge coordinates of a graph

The number of coordinates `Sym2 V` that are not edges of `G`.

Formalized by `StatMech.FK.ecz_NE`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ecz-ne).

## Each non-edge contributes a factor 2 to the partition function

`fkZ G p q = 2^{#non-edges} · ecz_fkZEdge G p q`: each non-edge coordinate contributes a free
factor
`2`.

Formalized by `StatMech.FK.ecz_factorization`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ecz-factorization).

## Interface subadditivity of $-\log$ of the edge partition function

`-log ecz_fkZEdge` is subadditive across an interface up to `|interface| · (-log(1 - p))`;
compare
`fis_neglog_interface_le` for `fkZ`.

Formalized by `StatMech.FK.ecz_neglog_interface_le`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean, line 314](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean#L314). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ecz-neglog-interface-le).

## Negative log edge partition function of a graph

`-log ecz_fkZEdge G p q`.

Formalized by `StatMech.FK.ecz_uu`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean, line 390](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean#L390). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ecz-uu).

## Negative log edge partition function of a box

`-log ecz_fkZEdge` of the box `Λ_n` at `p = logistic(t)`, `q = 2`.

Formalized by `StatMech.FK.ecz_u`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean, line 519](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean#L519). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ecz-u).

## Per-edge free energy of a box in the tilt variable

The per-edge free energy of `Λ_n` in the tilt variable, computed from `ecz_fkZEdge`.

Formalized by `StatMech.FK.ecz_edgeFreeEnergy`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean, line 607](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean#L607). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ecz-edge-free-energy).

## Additive doubling bound for the edge partition function

The doubling bound `agl_AdditiveDoublingBound` with `-log fkZ` replaced by `ecz_u`.

Formalized by `StatMech.FK.ecz_AdditiveDoublingBound`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean, line 646](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean#L646). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ecz-additive-doubling-bound).

## Boxes satisfy the additive doubling bound for $d \ge 1$

For `d ≥ 1`, `ecz_u` satisfies the doubling bound along the scales `K_j = 2^{j+1} - 1`.

Formalized by `StatMech.FK.ecz_additiveDoublingBound`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean, line 655](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean#L655). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ecz-additive-doubling-bound-2).

## Membership of a box vertex in a sub-box

A vertex of `Λ_n` lies in the sub-box `Λ_a`.

Formalized by `StatMech.FK.ecz_subBoxPred`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean, line 847](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean#L847). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ecz-sub-box-pred).

## Sub-box as an induced subgraph of a larger box

`Λ_a` is isomorphic to the subgraph of `Λ_n` induced on `Λ_a`.

Formalized by `StatMech.FK.ecz_subBoxIso`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean, line 854](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean#L854). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ecz-sub-box-iso).

## Convergence of the per-edge free energy of boxes

The per-edge free energy `ecz_u d s n / |E(Λ_n)|` converges as `n → ∞`.

Formalized by `StatMech.FK.ecz_PerEdgeDensityConverges`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean, line 1125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean#L1125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ecz-per-edge-density-converges).

## Number of sub-box translates along a side of a box

The number `⌊(2n + 1)/(2m + 1)⌋` of translates of `Λ_m` that fit along one side of `Λ_n`.

Formalized by `StatMech.FK.ecz_T`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean, line 1134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean#L1134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ecz-t).

## Center of a cell in the tiling of a box by sub-boxes

The center of the cell indexed by `c` in the tiling of `Λ_n` by translates of `Λ_m`.

Formalized by `StatMech.FK.ecz_center`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean, line 1140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean#L1140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ecz-center).

## Coordinate index of the tiling cell containing a site

The index along coordinate `i` of the tiling cell containing `x`.

Formalized by `StatMech.FK.ecz_cellIdx`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean, line 1164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean#L1164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ecz-cell-idx).

## Tiling cell of a box vertex

The tiling cell containing a vertex of `Λ_n`, or `none` if it lies in the leftover strip.

Formalized by `StatMech.FK.ecz_vanHoveTag`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean, line 1167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean#L1167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ecz-van-hove-tag).

## Translation between a sub-box and a tiling cell

The vertices of `Λ_m` correspond to the vertices of the cell `c` by translation.

Formalized by `StatMech.FK.ecz_cellEquiv`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean, line 1239](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean#L1239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ecz-cell-equiv).

## Graph isomorphism between a sub-box and a tiling cell

Each tiling cell induces a graph isomorphic to `Λ_m`.

Formalized by `StatMech.FK.ecz_cellBlockIso`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean, line 1253](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean#L1253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ecz-cell-block-iso).

## Restriction of a box to all tiling tags

Restricting `Λ_n` to all tags gives back `Λ_n`.

Formalized by `StatMech.FK.ecz_restUnivIso`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean, line 1282](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean#L1282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ecz-rest-univ-iso).

## Van Hove tiling bound for the edge partition function

Van Hove bound: `ecz_u d t n` is at most `T^d · ecz_u d t m` plus the cost of the leftover
strip
and of the interfaces between cells, where `T = ⌊(2n + 1)/(2m + 1)⌋`.

Formalized by `StatMech.FK.ecz_box_vanHove_subadd`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean, line 1291](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean#L1291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ecz-box-van-hove-subadd).

## Per-edge negative log edge partition function of a box

The per-edge free energy `ecz_u d s n / |E(Λ_n)|`.

Formalized by `StatMech.FK.ecz_f`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean, line 1434](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean#L1434). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ecz-f).

## Upper envelope for the per-edge free energy

An upper envelope for `ecz_f` combining the per-edge value at scale `m` with the all-closed
bound.

Formalized by `StatMech.FK.ecz_g`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean, line 1602](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean#L1602). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ecz-g).

## Per-edge free energy of boxes converges for $d \ge 1$

For `d ≥ 1`, the per-edge free energy `ecz_u d s n / |E(Λ_n)|` converges.

Formalized by `StatMech.FK.ecz_perEdgeDensityConverges`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean, line 1649](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean#L1649). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ecz-per-edge-density-converges-2).

## Vanishing block oscillation of the edge free energy

The edge free energy of `Λ_n` differs from that of `Λ_{K_{b(n)}}` by a vanishing oscillation.

Formalized by `StatMech.FK.ecz_BlockOscillation`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean, line 1943](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean#L1943). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ecz-block-oscillation).

## Per-box $q = 2$ uniqueness off a countable set of tilts

For `d ≥ 1`, a fixed box `Λ_N` with an edge witness, the free and wired `q = 2` measures
agree on every increasing event of `Λ_N` for all `t = logit(p)` outside a countable set in `t`.
This is the per-box `q = 2` case of `fkgq_countable_free_wired_disagreement`.

Formalized by `StatMech.FK.ecz_fk_uniqueness`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean, line 2112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdgePartitionFunction.lean#L2112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#ecz-fk-uniqueness).

## Secant bound gives $q = 2$ edge-event uniqueness off a countable set

For `q = 2`: assuming `φ^1_{p'}(e open) ≤ φ^0_p(e open)` for `p' < p` in `(0, 1)`, for all but
countably many `p` every measure between the free and wired infinite-volume measures on the
event
`{eb open}` agrees with both.

Formalized by `StatMech.FK.fk_uniqueness_off_countable_q2_full`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/UniquenessFromSecant.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/UniquenessFromSecant.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#fk-uniqueness-off-countable-q2-full).

## Convex limit of centered tilt free energies of boxes for $d, q \ge 1$

For `d ≥ 1` and `q ≥ 1`, the centered tilt free energies of the boxes `Λ_n` converge pointwise
to
a convex function `G` with `G(0) = 0`.

Formalized by `StatMech.FK.fkgq_centeredConvergence`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/UniquenessGeneralQ.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/UniquenessGeneralQ.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#fkgq-centered-convergence).

## Average edge density of a random-cluster measure

The average edge density `|E|^{-1} E_{φ_{G,p,q}}[#open edges]` at `p = logistic(s)`.

Formalized by `StatMech.FK.fkgq_avgDensity`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/UniquenessGeneralQ.lean, line 332](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/UniquenessGeneralQ.lean#L332). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#fkgq-avg-density).

## Free infinite-volume mass function on a box for $q \ge 1$

The mass function on configurations of `Λ_N` of the free infinite-volume measure at
`p = logistic(s)`.

Formalized by `StatMech.FK.fkgq_freeMass`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/UniquenessGeneralQ.lean, line 495](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/UniquenessGeneralQ.lean#L495). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#fkgq-free-mass).

## Wired infinite-volume mass function on a box for $q \ge 1$

The mass function on configurations of `Λ_N` of the wired infinite-volume measure at
`p = logistic(s)`.

Formalized by `StatMech.FK.fkgq_wiredMass`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/UniquenessGeneralQ.lean, line 504](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/UniquenessGeneralQ.lean#L504). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#fkgq-wired-mass).

## Free unit-edge marginal at $0$ on $\Lambda_{\lfloor\sqrt n\rfloor}$

The free marginal on `Λ_{⌊√n⌋}` of the unit edge at the origin in direction `dir`, at
`p = logistic(t)`.

Formalized by `StatMech.FK.fkgq_unitMarg`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/UniquenessGeneralQ.lean, line 1184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/UniquenessGeneralQ.lean#L1184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#fkgq-unit-marg).

## Wired unit-edge marginal at $0$ on $\Lambda_{\lfloor\sqrt n\rfloor}$

The wired marginal on `Λ_{⌊√n⌋}` of the unit edge at the origin in direction `dir`, at
`p = logistic(t)`.

Formalized by `StatMech.FK.fkgq_unitWiredMarg`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/UniquenessGeneralQ.lean, line 1194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/UniquenessGeneralQ.lean#L1194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#fkgq-unit-wired-marg).

## Total deviation of free unit-edge marginals from a free density

The total deviation between the free density of `e` and the free unit-edge marginals on
`Λ_{⌊√n⌋}`, summed over directions.

Formalized by `StatMech.FK.fkgq_freeDelta`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/UniquenessGeneralQ.lean, line 1262](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/UniquenessGeneralQ.lean#L1262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#fkgq-free-delta).

## Total deviation of wired unit-edge marginals from a wired density

The total deviation between the wired unit-edge marginals on `Λ_{⌊√n⌋}` and the wired density
of
`e`, summed over directions.

Formalized by `StatMech.FK.fkgq_wiredDelta`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/UniquenessGeneralQ.lean, line 1271](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/UniquenessGeneralQ.lean#L1271). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#fkgq-wired-delta).

## Per-box uniqueness of the random-cluster measures off a countable set

For `d ≥ 1`,
`q ≥ 1`, and every box `Λ_N`, the free and wired infinite-volume random-cluster measures on
`ℤ^d` at `p = logistic(t)` give the same mass to every increasing event of `Λ_N`, for all `t`
outside a countable set.

This is a per-box statement only: the countable exceptional set may depend on `N`, the
statement is in the logit parameter `t` rather than in `p ∈ (0, 1)` directly, and it concludes
agreement on increasing events of that one finite restriction, not equality of the
infinite-volume measures. No declaration here takes the countable union over `N`, transfers
it to `p`, or derives equality of the infinite-volume measures. (Grimmett, *The Random-Cluster
Model*, 2006, Theorem 4.60.)

Formalized by `StatMech.FK.fkgq_countable_free_wired_disagreement`, a theorem declared in [PhyslibExt/StatisticalMechanics/RandomCluster/UniquenessGeneralQ.lean, line 1726](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/UniquenessGeneralQ.lean#L1726). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html#fkgq-countable-free-wired-disagreement).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Per-box agreement of free and wired random-cluster measures](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/random-cluster-model/per-box-agreement-of-free-and-wired-random-clust)
