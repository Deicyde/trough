---
declaration: section
origin: cited
lean: StatMech.FK.outProj, StatMech.FK.outProj_eq_false_of_range, StatMech.FK.outProj_eq_of_not_range, StatMech.FK.agreesOff_outProj, StatMech.FK.outProj_idem, StatMech.FK.filter_outProj_eq_condFibre, StatMech.FK.condFibre_congr_dom, StatMech.FK.condBcProb_congr_dom
statement: formalized
proof: formalized
---

# Wired random-cluster measures decrease with the box

48 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html).

## A. Conditioning on the configuration outside the inner box

## Outer part of a configuration on $\Lambda_{n+1}$

Project a configuration on `Λ_(n+1)` to its outer part: edges of `Λ_n` closed, the others
unchanged.

Formalized by `StatMech.FK.outProj`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#out-proj).

## Outer projection closes the edges of $\Lambda_n$

The projection closes edges of `Λ_n`.

Formalized by `StatMech.FK.outProj_eq_false_of_range`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#out-proj-eq-false-of-range).

## Outer projection keeps the edges outside $\Lambda_n$

The projection keeps edges outside `Λ_n`.

Formalized by `StatMech.FK.outProj_eq_of_not_range`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#out-proj-eq-of-not-range).

## Outer projection agrees with the configuration off $\Lambda_n$

The projection agrees with the configuration off the edges of `Λ_n`.

Formalized by `StatMech.FK.agreesOff_outProj`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#agrees-off-out-proj).

## Outer projection is idempotent

The projection is idempotent.

Formalized by `StatMech.FK.outProj_idem`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#out-proj-idem).

## Configurations with a given outer part form its conditioning fibre

The configurations with outer part `ψ` form the conditioning fibre of `ψ`.

Formalized by `StatMech.FK.filter_outProj_eq_condFibre`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#filter-out-proj-eq-cond-fibre).

## Configurations agreeing off $F$ have the same conditioning fibre

Configurations agreeing off `F` have the same conditioning fibre.

Formalized by `StatMech.FK.condFibre_congr_dom`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#cond-fibre-congr-dom).

## Configurations agreeing off $F$ have equal conditional probabilities

Configurations agreeing off `F` give the same conditional random-cluster probabilities.

Formalized by `StatMech.FK.condBcProb_congr_dom`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#cond-bc-prob-congr-dom).

## Masses of the conditioning fibres sum to one

The masses of the conditioning fibres over all outer configurations sum to `1`.

Formalized by `StatMech.FK.sum_fibreMass_eq_one`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#sum-fibre-mass-eq-one).

## Wired $\Lambda_{n+1}$ measure decomposed over outer configurations

Decomposition of the wired measure on `Λ_(n+1)` over the configuration outside `Λ_n`.

Formalized by `StatMech.FK.wiredSucc_bcProb_decompose`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#wired-succ-bc-prob-decompose).

## Conditional wired decrease on inner increasing events for $q \ge 1$

For `q ≥ 1`, conditionally on any outer configuration, the wired measure on `Λ_(n+1)` gives an
increasing event of `Λ_n` at most its wired `Λ_n` probability.

Formalized by `StatMech.FK.condBcProb_innerRestrict_le`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#cond-bc-prob-inner-restrict-le).

## Wired box measures decrease on inner increasing events for $q \ge 1$

For `q ≥ 1`, the wired measure on `Λ_(n+1)` gives an increasing event of `Λ_n` at most its wired
`Λ_n` probability.

Formalized by `StatMech.FK.wiredSucc_bcProb_innerEvent_le`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#wired-succ-bc-prob-inner-event-le).

## Wired $\Lambda_{n+1}$ measure of a $\Lambda_n$ cylinder event as a sum

The wired `Λ_(n+1)` measure of a `Λ_n` cylinder event, as a finite sum.

Formalized by `StatMech.FK.wiredFiniteMeasure_succ_real_innerRestrictEvent`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#wired-finite-measure-succ-real-inner-res).

## Wired box measures decrease on increasing cylinder events at $q = 2$

For `q = 2`, the wired `Λ_(n+1)` measure of an increasing `Λ_n` cylinder event is at most its
wired `Λ_n` probability.

Formalized by `StatMech.FK.wiredFiniteMeasure_succ_le_smallerBox`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 298](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L298). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#wired-finite-measure-succ-le-smaller-box).

## Origin-to-boundary connection is an increasing event

The event that the origin is connected to the box boundary is increasing.

Formalized by `StatMech.FK.isIncreasing_connToBdryEvent`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 311](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L311). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#is-increasing-conn-to-bdry-event).

## Wired $q = 2$ probability of $0 \leftrightarrow \partial\Lambda_n$ in $\Lambda_{n+1}$ at most in $\Lambda_n$

For `q = 2`, `φ¹_{Λ_(n+1)}(0 ↔ ∂Λ_n) ≤ φ¹_{Λ_n}(0 ↔ ∂Λ_n)`.

Formalized by `StatMech.FK.wiredFiniteMeasure_succ_le_boxBdryConnEvent`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#wired-finite-measure-succ-le-box-bdry-co).

## Open edges of $\Lambda_n$ are open edges of $\Lambda_{n+1}$

An open edge of `Λ_n` is an open edge of `Λ_(n+1)`.

Formalized by `StatMech.FK.openSub_succ_adj_inner`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 335](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L335). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#open-sub-succ-adj-inner).

## Inner vertices next to the annulus lie on $\partial\Lambda_n$

A vertex of `Λ_n` adjacent to a vertex of `Λ_(n+1) \ Λ_n` lies on `∂Λ_n`.

Formalized by `StatMech.FK.boxBoundary_of_openSub_succ_adj_outer`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 349](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L349). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#box-boundary-of-open-sub-succ-adj-outer).

## Box inclusion maps the origin to the origin

The inclusion `Λ_n → Λ_(n+1)` maps the origin to the origin.

Formalized by `StatMech.FK.boxVertIncl_boxOrigin`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 361](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L361). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#box-vert-incl-box-origin).

## Paths to $\partial\Lambda_{n+1}$ pass through $\partial\Lambda_n$

A connection from the origin to `∂Λ_(n+1)` inside `Λ_(n+1)` passes through `∂Λ_n`.

Formalized by `StatMech.FK.connToBdry_succ_of_connToBdry`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 366](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L366). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#conn-to-bdry-succ-of-conn-to-bdry).

## One-step decrease of the events $0 \leftrightarrow \partial\Lambda_n$

The events `0 ↔ ∂Λ_n` decrease in `n`.

Formalized by `StatMech.FK.boxBdryConnEvent_succ_subset`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 400](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L400). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#box-bdry-conn-event-succ-subset).

## Wired $q = 2$ probability of $0 \leftrightarrow \partial\Lambda_n$ in $\Lambda_n$ is nonincreasing in $n$

For `q = 2`, `φ¹_{Λ_(n+1)}(0 ↔ ∂Λ_(n+1)) ≤ φ¹_{Λ_n}(0 ↔ ∂Λ_n)`.

Formalized by `StatMech.FK.wiredFiniteMeasure_boxBdryConnEvent_antitone`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 408](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L408). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#wired-finite-measure-box-bdry-conn-event).

## Inclusion of $\Lambda_n$ into $\Lambda_m$ for $n \le m$

The inclusion `Λ_n → Λ_m` for `n ≤ m`.

Formalized by `StatMech.FK.boxVertInclLE`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 420](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L420). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#box-vert-incl-le).

## Inclusion of edges of $\Lambda_n$ into edges of $\Lambda_m$

The inclusion of edges of `Λ_n` into edges of `Λ_m` for `n ≤ m`.

Formalized by `StatMech.FK.innerEdgeLE`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 424](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L424). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#inner-edge-le).

## Edge inclusion into $\mathbb{Z}^d$ factors through $\Lambda_m$

Including an edge into `Λ_m` and then into `ℤ^d` is including it into `ℤ^d`.

Formalized by `StatMech.FK.edgeIncl_innerEdgeLE`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 428](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L428). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#edge-incl-inner-edge-le).

## Restriction of a configuration from $\Lambda_m$ to $\Lambda_n$

Restrict a configuration on `Λ_m` to `Λ_n` for `n ≤ m`.

Formalized by `StatMech.FK.boxRestrictLE`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 435](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L435). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#box-restrict-le).

## Restriction to $\Lambda_n$ factors through $\Lambda_m$

Restricting to `Λ_m` and then to `Λ_n` is restricting to `Λ_n`.

Formalized by `StatMech.FK.boxRestrictLE_boxRestrict`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 440](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L440). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#box-restrict-le-box-restrict).

## Monotonicity of restriction between boxes

Restriction between boxes is monotone.

Formalized by `StatMech.FK.boxRestrictLE_monotone`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 448](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L448). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#box-restrict-le-monotone).

## Boundary-connection event of $\Lambda_n$ as an event on $\Lambda_m$

The event `0 ↔ ∂Λ_n` inside `Λ_n`, as an event on `Λ_m` for `n ≤ m`.

Formalized by `StatMech.FK.connToBdryEventLE`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 453](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L453). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#conn-to-bdry-event-le).

## Boundary-connection event of $\Lambda_n$ on $\Lambda_m$ is increasing

The event `connToBdryEventLE` is increasing.

Formalized by `StatMech.FK.isIncreasing_connToBdryEventLE`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 459](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L459). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#is-increasing-conn-to-bdry-event-le).

## Boundary connection of $\Lambda_n$ is a $\Lambda_m$ cylinder event

The event `0 ↔ ∂Λ_n` is a `Λ_m` cylinder event for every `m ≥ n`.

Formalized by `StatMech.FK.boxBdryConnEvent_eq_boxRestrict_preimage`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 467](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L467). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#box-bdry-conn-event-eq-box-restrict-prei).

## Cylinder form of the $\Lambda_n$ boundary connection is measurable

The cylinder form of `0 ↔ ∂Λ_n` is measurable.

Formalized by `StatMech.FK.measurableSet_boxRestrict_connToBdryEventLE`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 474](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L474). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#measurable-set-box-restrict-conn-to-bdry).

## Wired $\Lambda_m$ measure of a $\Lambda_m$ cylinder event as a sum

The wired `Λ_m` measure of a `Λ_m` cylinder event, as a finite sum.

Formalized by `StatMech.FK.wiredFiniteMeasure_real_boxRestrictEvent`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 480](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L480). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#wired-finite-measure-real-box-restrict-e).

## Wired $q = 2$ probability of $0 \leftrightarrow \partial\Lambda_n$ in $\Lambda_{m+1}$ at most in $\Lambda_m$, $m \ge n$

For `q = 2` and `n ≤ m`, `φ¹_{Λ_(m+1)}(0 ↔ ∂Λ_n) ≤ φ¹_{Λ_m}(0 ↔ ∂Λ_n)`.

Formalized by `StatMech.FK.wiredFiniteMeasure_succ_le_boxBdryConnEvent_le`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 502](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L502). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#wired-finite-measure-succ-le-box-bdry-co-2).

## Wired $q = 2$ probability of $0 \leftrightarrow \partial\Lambda_n$ in $\Lambda_{n+k+1}$ at most in $\Lambda_{n+k}$

For `q = 2`, `φ¹_{Λ_(n+k+1)}(0 ↔ ∂Λ_n) ≤ φ¹_{Λ_(n+k)}(0 ↔ ∂Λ_n)`.

Formalized by `StatMech.FK.wiredFiniteMeasure_boxBdryConnEvent_antitone_radius`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 516](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L516). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#wired-finite-measure-box-bdry-conn-event-2).

## Open edges of a box are open edges of $\mathbb{Z}^d$

An open edge of the box is an open edge of `ℤ^d`.

Formalized by `StatMech.FK.openSubgraph_adj_of_boxGraph`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 527](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L527). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#open-subgraph-adj-of-box-graph).

## Open connections in a box are open connections in $\mathbb{Z}^d$

An open connection inside the box is an open connection in `ℤ^d`.

Formalized by `StatMech.FK.connected_of_boxConnected`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 542](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L542). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#connected-of-box-connected).

## Boundary connection inside $\Lambda_n$ reaches outside $\Lambda_{n-1}$

A connection from the origin to `∂Λ_n` inside `Λ_n` reaches the complement of `Λ_(n-1)`.

Formalized by `StatMech.FK.boxBdryConnEvent_subset_crossingEvent`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 554](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L554). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#box-bdry-conn-event-subset-crossing-even).

## Open lattice edges between box vertices are open box edges

An open edge of `ℤ^d` between box vertices is an open edge of the box.

Formalized by `StatMech.FK.boxGraph_open_of_openSubgraph`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 565](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L565). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#box-graph-open-of-open-subgraph).

## Open path from the origin out of $\Lambda_n$ gives $0 \leftrightarrow \partial\Lambda_n$ inside $\Lambda_n$

A connection from the origin to a site outside `Λ_n` gives a connection to `∂Λ_n` inside `Λ_n`.

Formalized by `StatMech.FK.boxBdryConn_of_crossing`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 579](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L579). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#box-bdry-conn-of-crossing).

## Leaving $\Lambda_n$ implies connecting to $\partial\Lambda_n$

Reaching the complement of `Λ_n` implies `0 ↔ ∂Λ_n`.

Formalized by `StatMech.FK.crossingEvent_succ_subset_boxBdryConnEvent`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 610](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L610). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#crossing-event-succ-subset-box-bdry-conn).

## Wired infinite-volume boundary connection tends to $\theta^1(p, q)$

Under the wired infinite-volume measure, `P(0 ↔ ∂Λ_n) → θ¹(p, q)`.

Formalized by `StatMech.FK.wiredIv_boxBdryConnEvent_tendsto`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 620](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L620). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#wired-iv-box-bdry-conn-event-tendsto).

## Events $0 \leftrightarrow \partial\Lambda_n$ decrease in $n \ge 1$

The events `0 ↔ ∂Λ_n` decrease in `n ≥ 1`.

Formalized by `StatMech.FK.boxBdryConnEvent_subset_le`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 641](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L641). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#box-bdry-conn-event-subset-le).

## Wired $q = 2$ probability of $0 \leftrightarrow \partial\Lambda_k$ in $\Lambda_{k+j}$ is nonincreasing in $j$

For `q = 2`, `j ↦ φ¹_{Λ_(k+j)}(0 ↔ ∂Λ_k)` is antitone.

Formalized by `StatMech.FK.radius_antitone`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 651](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L651). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#radius-antitone).

## Antitone bounded-below sequences converge to any subsequential limit

A bounded-below antitone real sequence converges to the limit of any of its subsequences.

Formalized by `StatMech.FK.tendsto_of_antitone_of_subseq`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 661](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L661). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#tendsto-of-antitone-of-subseq).

## Infinite-volume limit of the wired $q = 2$ probability of $0 \leftrightarrow \partial\Lambda_k$

For `q = 2`, `φ¹_{Λ_(k+j)}(0 ↔ ∂Λ_k)` converges as `j → ∞` to the wired infinite-volume
probability of `0 ↔ ∂Λ_k`.

Formalized by `StatMech.FK.wiredFiniteMeasure_radius_tendsto`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 671](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L671). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#wired-finite-measure-radius-tendsto).

## Wired $q = 2$ percolation probability as the limit of $0 \leftrightarrow \partial\Lambda_n$ in $\Lambda_n$

For `q = 2`, `φ¹_{Λ_n}(0 ↔ ∂Λ_n) → θ¹(p, 2)`.

Formalized by `StatMech.FK.boxBdryConnEvent_diag_tendsto`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 707](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L707). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#box-bdry-conn-event-diag-tendsto).

## Ising FK box-boundary connection profile tends to $\theta^1(p, 2)$

The box-boundary connection profile of the Ising FK representation converges to `θ¹(p, 2)`.

Formalized by `StatMech.FK.boxBoundaryConnProfile_tendsto`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean, line 755](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDomChain.lean#L755). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html#box-boundary-conn-profile-tendsto).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Wired random-cluster measures decrease with the box](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/wired-random-cluster-measures-decrease-with-the)
