---
declaration: section
origin: cited
lean: StatMech.FK.horizWalk, StatMech.FK.exists_far_not_mem, StatMech.FK.exists_walk_exterior, StatMech.FK.closedCircuitEvent, StatMech.FK.exists_closed_latticeCircuit_of_finite_cluster, StatMech.FK.exists_enclosing_closed_latticeCircuit_of_finite_cluster, StatMech.FK.finiteCluster_subset_iUnion_closedCircuit, StatMech.FK.compl_percolationEvent_eq_finiteCluster
statement: formalized
proof: formalized
---

# The random-cluster critical point on ℤ² is below one, given a Peierls bound

25 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-random-cluster-critical-point-on-is-below-on/index.html).

## A. Walks to the exterior of a finite cluster

## Horizontal lattice walk in $\mathbb{Z}^2$

The horizontal lattice walk of `k` steps from `(a, c)` to `(a + k, c)` in `ℤ²`.

Formalized by `StatMech.FK.horizWalk`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-random-cluster-critical-point-on-is-below-on/index.html#horiz-walk).

## Finite subsets of $\mathbb{Z}^2$ miss far points on each row

A finite set of `ℤ²` misses some point `(N, c)` with `N ≥ a₀` on every horizontal line.

Formalized by `StatMech.FK.exists_far_not_mem`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-random-cluster-critical-point-on-is-below-on/index.html#exists-far-not-mem).

## Finite cluster in $\mathbb{Z}^2$ has a reachable point outside it

A finite cluster of `o` has a lattice-reachable point outside it.

Formalized by `StatMech.FK.exists_walk_exterior`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-random-cluster-critical-point-on-is-below-on/index.html#exists-walk-exterior).

## Closed-circuit event of a dual circuit

The event that every primal edge crossed by the dual circuit `c` is closed.

Formalized by `StatMech.FK.closedCircuitEvent`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-random-cluster-critical-point-on-is-below-on/index.html#closed-circuit-event).

## Finite cluster in $\mathbb{Z}^2$ gives a closed lattice circuit

A finite open cluster of `o` in `ℤ²` is surrounded by a lattice cycle whose crossed primal edges
are all closed.

Formalized by `StatMech.FK.exists_closed_latticeCircuit_of_finite_cluster`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-random-cluster-critical-point-on-is-below-on/index.html#exists-closed-lattice-circuit-of-finite).

## Finite cluster in $\mathbb{Z}^2$: closed circuit, separated point, odd crossings

The closed circuit of `exists_closed_latticeCircuit_of_finite_cluster`, together with a point
that the cluster boundary separates from `o` and an odd crossing number for every walk to it.

Formalized by `StatMech.FK.exists_enclosing_closed_latticeCircuit_of_finite_cluster`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-random-cluster-critical-point-on-is-below-on/index.html#exists-enclosing-closed-lattice-circuit).

## Finite-cluster event is covered by closed-circuit events

The event that the cluster of `o` is finite is covered by the closed-circuit events.

Formalized by `StatMech.FK.finiteCluster_subset_iUnion_closedCircuit`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-random-cluster-critical-point-on-is-below-on/index.html#finite-cluster-subset-i-union-closed-cir).

## Non-percolation means the origin's cluster is finite

No percolation from the origin means the cluster of the origin is finite.

Formalized by `StatMech.FK.compl_percolationEvent_eq_finiteCluster`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-random-cluster-critical-point-on-is-below-on/index.html#compl-percolation-event-eq-finite-cluste).

## Peierls series $\sum_\ell \ell\,(2d)^\ell (1-p)^\ell$

The Peierls series `Σ_ℓ ℓ (2d)^ℓ (1 - p)^ℓ` bounding the probability of a finite cluster.

Formalized by `StatMech.FK.fkPcUpperBound`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-random-cluster-critical-point-on-is-below-on/index.html#fk-pc-upper-bound).

## Ratio $2d(1-p)$ of the Peierls series

The ratio `2d (1 - p)` of the Peierls series.

Formalized by `StatMech.FK.fkPcRatio`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-random-cluster-critical-point-on-is-below-on/index.html#fk-pc-ratio).

## Defining formula for the Peierls ratio

Unfolding `fkPcRatio`.

Formalized by `StatMech.FK.fkPcRatio_def`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-random-cluster-critical-point-on-is-below-on/index.html#fk-pc-ratio-def).

## Peierls summand as $\ell x^\ell$ with $x = 2d(1-p)$

The Peierls summand in terms of `fkPcRatio`.

Formalized by `StatMech.FK.fkPcSummand_eq`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-random-cluster-critical-point-on-is-below-on/index.html#fk-pc-summand-eq).

## Closed form $x/(1-x)^2$ of the Peierls series for $|x| < 1$

Closed form `x / (1 - x)²` of the Peierls series for `|x| < 1`, where `x = 2d (1 - p)`.

Formalized by `StatMech.FK.fkPcUpperBound_eq_closedForm`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-random-cluster-critical-point-on-is-below-on/index.html#fk-pc-upper-bound-eq-closed-form).

## Peierls ratio $2d(1-p)$ tends to $0$ as $p \to 1$

`2d (1 - p) → 0` as `p → 1`.

Formalized by `StatMech.FK.fkPcRatio_tendsto_one`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-random-cluster-critical-point-on-is-below-on/index.html#fk-pc-ratio-tendsto-one).

## $x/(1-x)^2 \to 0$ as $x \to 0$

`x / (1 - x)² → 0` as `x → 0`.

Formalized by `StatMech.FK.fkPcClosedForm_tendsto_zero`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-random-cluster-critical-point-on-is-below-on/index.html#fk-pc-closed-form-tendsto-zero).

## Peierls series tends to $0$ as $p \to 1$

The Peierls series tends to `0` as `p → 1`.

Formalized by `StatMech.FK.fkPcUpperBound_tendsto_one`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-random-cluster-critical-point-on-is-below-on/index.html#fk-pc-upper-bound-tendsto-one).

## Peierls series is below 1 on an interval $(p_0, 1)$

The Peierls series is below `1` on an interval `(p₀, 1]`.

Formalized by `StatMech.FK.exists_p_lt_one_fkPcUpperBound_lt_one`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-random-cluster-critical-point-on-is-below-on/index.html#exists-p-lt-one-fk-pc-upper-bound-lt-one).

## Nonnegativity of the Peierls series for $p \le 1$

The Peierls series is nonnegative for `p ≤ 1`.

Formalized by `StatMech.FK.fkPcUpperBound_nonneg`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-random-cluster-critical-point-on-is-below-on/index.html#fk-pc-upper-bound-nonneg).

## Peierls bound hypothesis for the wired measure on $\mathbb{Z}^2$

The Peierls bound for the wired random-cluster measure on `ℤ²` at `(p, q)`:
`1 - θ¹(p, q) ≤ Σ_ℓ ℓ 4^ℓ (1 - p)^ℓ`.

Formalized by `StatMech.FK.FkNonPercolationBound`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-random-cluster-critical-point-on-is-below-on/index.html#fk-non-percolation-bound).

## Percolation from a Peierls bound with series below 1

The Peierls bound with a series below `1` gives percolation: `0 < θ¹(p, q)`.

Formalized by `StatMech.FK.fkTheta_pos_of_nonPercolationBound`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-random-cluster-critical-point-on-is-below-on/index.html#fk-theta-pos-of-non-percolation-bound).

## Nonempty subcritical set on $\mathbb{Z}^2$ for $q \ge 1$

For `q ≥ 1` the subcritical set on `ℤ²` is nonempty (it contains `1/8`).

Formalized by `StatMech.FK.fkSubcriticalSet_nonempty`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-random-cluster-critical-point-on-is-below-on/index.html#fk-subcritical-set-nonempty).

## Positive percolation probability rules out subcriticality

A parameter with positive percolation probability is not subcritical.

Formalized by `StatMech.FK.not_mem_fkSubcriticalSet_of_fkTheta_pos`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean, line 266](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean#L266). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-random-cluster-critical-point-on-is-below-on/index.html#not-mem-fk-subcritical-set-of-fk-theta-p).

## $p_c(q) < 1$ on $\mathbb{Z}^2$ for $q \ge 1$ under a Peierls bound

For `q ≥ 1`, the random-cluster critical point on `ℤ²` satisfies `p_c(q) < 1`, assuming the
Peierls bound `FkNonPercolationBound` for all `p` in some interval `(p₀, 1)`.

Formalized by `StatMech.FK.fkPc_lt_one`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-random-cluster-critical-point-on-is-below-on/index.html#fk-pc-lt-one).

## $0 < p_c(q) < 1$ on $\mathbb{Z}^2$ for $q \ge 1$ under a Peierls bound

For `q ≥ 1`, `0 < p_c(q) < 1` on `ℤ²`, assuming the Peierls bound as in `fkPc_lt_one`.

Formalized by `StatMech.FK.fkPc_pos_and_lt_one`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean, line 310](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean#L310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-random-cluster-critical-point-on-is-below-on/index.html#fk-pc-pos-and-lt-one).

## Peierls series for $d = 2$ equals the Bernoulli Peierls series

The Peierls series for `d = 2` is the Bernoulli Peierls series
`StatMech.Percolation.pcUpperBound`.

Formalized by `StatMech.FK.fkPcUpperBound_two_eq_pcUpperBound`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean, line 319](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcLtOnePeierls.lean#L319). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-random-cluster-critical-point-on-is-below-on/index.html#fk-pc-upper-bound-two-eq-pc-upper-bound).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The random-cluster critical point on ℤ² is below one, given a Peierls bound](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-random-cluster-critical-point-on-is-below-on/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-random-cluster-critical-point-on-is-below-on)
