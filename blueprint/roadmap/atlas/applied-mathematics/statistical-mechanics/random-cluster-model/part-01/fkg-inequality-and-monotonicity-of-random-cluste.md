---
declaration: section
origin: cited
lean: StatMech.FK.edgeMarginalOpen, StatMech.FK.edge_density_bounds, StatMech.FK.card_connectedComponent_submodular, StatMech.FK.numClusters_supermodular, StatMech.FK.fkProb_FKGLatticeCondition, StatMech.FK.fkProb_positively_associated, StatMech.FK.fkProb_positively_associated_events, StatMech.FK.kerLap
statement: formalized
proof: formalized
---

# FKG inequality and monotonicity of random-cluster measures

51 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html).

## Probability that an edge is open under the random-cluster measure

The probability `φ_{G,p,q}(e open)` that the edge `e` is open.

Formalized by `StatMech.FK.edgeMarginalOpen`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/DensityBounds.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/DensityBounds.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#edge-marginal-open).

## Edge density lies between $p/(p+q(1-p))$ and $p$ for $q \ge 1$

For `q ≥ 1`, every edge of `G` is open with probability between `p / (p + q(1 - p))` and `p`.

Formalized by `StatMech.FK.edge_density_bounds`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/DensityBounds.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/DensityBounds.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#edge-density-bounds).

## Supermodularity of the number of connected components

The number of connected components of simple graphs on a finite vertex set is supermodular:
`#comp(G₁) + #comp(G₂) ≤ #comp(G₁ ⊔ G₂) + #comp(G₁ ⊓ G₂)`.

Formalized by `StatMech.FK.card_connectedComponent_submodular`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FKG.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FKG.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#card-connected-component-submodular).

## Supermodularity of the random-cluster cluster count

The cluster count of the random-cluster model is supermodular in the configuration.

Formalized by `StatMech.FK.numClusters_supermodular`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FKG.lean, line 304](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FKG.lean#L304). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#num-clusters-supermodular).

## FKG lattice condition for the random-cluster measure

For `q ≥ 1` and `p ∈ (0, 1)`, the random-cluster measure satisfies the FKG lattice condition
`φ(a) φ(b) ≤ φ(a ⊔ b) φ(a ⊓ b)`.

Formalized by `StatMech.FK.fkProb_FKGLatticeCondition`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FKG.lean, line 364](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FKG.lean#L364). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#fk-prob-fkglattice-condition).

## FKG inequality for the random-cluster model

For `q ≥ 1`, increasing functions are positively
correlated under `φ_{G,p,q}`: `φ(f) φ(g) ≤ φ(f g)`.
(Fortuin–Kasteleyn–Ginibre, Comm. Math. Phys. 22, 1971; Grimmett, *The Random-Cluster Model*,
2006,
Theorem 3.8.)

Formalized by `StatMech.FK.fkProb_positively_associated`, a theorem declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FKG.lean, line 381](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FKG.lean#L381). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#fk-prob-positively-associated).

## FKG inequality for increasing random-cluster events

The FKG inequality for increasing events: `φ(A) φ(B) ≤ φ(A ∩ B)` for `q ≥ 1`.

Formalized by `StatMech.FK.fkProb_positively_associated_events`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FKG.lean, line 392](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FKG.lean#L392). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#fk-prob-positively-associated-events).

## Kernel of the Laplacian of the open subgraph

The kernel of the Laplacian of the open subgraph of `ω`, a subspace of `V → ℝ`.

Formalized by `StatMech.FK.kerLap`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/Comparison.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/Comparison.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#ker-lap).

## Number of open clusters equals the dimension of the Laplacian kernel

The number of open clusters equals the dimension of the kernel of the Laplacian of the open
subgraph.

Formalized by `StatMech.FK.numClusters_eq_finrank`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/Comparison.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/Comparison.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#num-clusters-eq-finrank).

## Holley's cross inequality for FK measures, $p_1 \le p_2$, $q \ge 1$

Holley's cross inequality for two random-cluster measures with `p₁ ≤ p₂` and the same `q ≥ 1`.

Formalized by `StatMech.FK.fkProb_cross`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/Comparison.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/Comparison.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#fk-prob-cross).

## Monotonicity of the random-cluster measure in `p`

For `q ≥ 1` and `p₁ ≤ p₂`,
`φ_{p₁,q}(A) ≤ φ_{p₂,q}(A)` for every increasing event `A`
(Grimmett, *The Random-Cluster Model*, 2006, Theorem 3.21).

Formalized by `StatMech.FK.fkProb_stochastically_increasing`, a theorem declared in [PhyslibExt/StatisticalMechanics/RandomCluster/Comparison.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/Comparison.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#fk-prob-stochastically-increasing).

## Number of open edges of a configuration

The number of open edges of `G` in `ω`. Same as `openCount` in `Tilt`.

Formalized by `StatMech.FK.chOpenCount`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/ComparisonHolley.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/ComparisonHolley.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#ch-open-count).

## Edges closed in one configuration and open in another

The edges of `G` closed in `b` and open in `c`.

Formalized by `StatMech.FK.diffSet`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/ComparisonHolley.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/ComparisonHolley.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#diff-set).

## Cluster count plus open-edge count is monotone

For `b ≤ c`, `k(b) + o(b) ≤ k(c) + o(c)`: opening an edge lowers the cluster count by at most
one.

Formalized by `StatMech.FK.numClusters_add_openCount_mono`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/ComparisonHolley.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/ComparisonHolley.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#num-clusters-add-open-count-mono).

## Reduced density $p/(p + q(1-p))$

The reduced density `p / (p + q(1 - p))`: the Bernoulli parameter dominated by `φ_{p,q}`.

Formalized by `StatMech.FK.reducedDensity`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/ComparisonHolley.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/ComparisonHolley.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#reduced-density).

## Random-cluster measure increases stochastically in $p$ when $q \ge 1$

For `q ≥ 1` the random-cluster measure is stochastically increasing in `p`.

Formalized by `StatMech.FK.fk_monotone_in_p`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/ComparisonHolley.lean, line 400](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/ComparisonHolley.lean#L400). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#fk-monotone-in-p).

## Comparison inequalities

For `q ≥ 1`,
`P_{p/(p + q(1 - p))} ≼ φ_{p,q} ≼ P_p`, with every law extended uniformly to loops
and nonedges. On graph-edge marginals, this gives the usual FK/Bernoulli comparison
(Fortuin 1972; Grimmett, *The Random-Cluster Model*, 2006, Theorem 3.21).

Formalized by `StatMech.FK.fk_bernoulli_sandwich`, a theorem declared in [PhyslibExt/StatisticalMechanics/RandomCluster/ComparisonHolley.lean, line 432](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/ComparisonHolley.lean#L432). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#fk-bernoulli-sandwich).

## Mixed supermodularity of free and wired cluster counts

Mixed supermodularity of cluster counts: `k(a) + k¹(b) ≤ k(a ⊓ b) + k¹(a ⊔ b)`, where `k¹`
counts clusters with the boundary wired.

Formalized by `StatMech.FK.mixed_supermodular`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/Limits.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/Limits.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#mixed-supermodular).

## Holley's condition for free and wired weights when $q \ge 1$

Holley's condition for the free and wired weights when `q ≥ 1`. See also `bcWeight_cross`, which
contains this as the case of boundary wirings `⊥ ≤ clique`.

Formalized by `StatMech.FK.freeWiredWeight_cross`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/Limits.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/Limits.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#free-wired-weight-cross).

## Holley's condition for free and wired probabilities when $q \ge 1$

Holley's condition for the free and wired probabilities when `q ≥ 1`.

Formalized by `StatMech.FK.freeWiredProb_cross`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/Limits.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/Limits.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#free-wired-prob-cross).

## Free–wired domination on a finite graph for $q \ge 1$

For `q ≥ 1` the free random-cluster measure gives every increasing event at most the probability
the wired measure gives it.

Formalized by `StatMech.FK.fkProb_le_wiredFkProb_increasing`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/Limits.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/Limits.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#fk-prob-le-wired-fk-prob-increasing).

## Free box measure dominated by the wired one for $q \ge 1$

For `q ≥ 1` the free box measure is stochastically dominated by the wired box measure on `ℤ^d`:
`φ⁰_n ≼ φ¹_n`.

Formalized by `StatMech.FK.freeFiniteMeasure_dominated`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/Limits.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/Limits.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#free-finite-measure-dominated).

## Number of clusters under a boundary wiring

The number of clusters of `ω` under the boundary wiring `C`: connected components of the open
subgraph of `ω` joined with `C`.

Formalized by `StatMech.FK.numClustersBC`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/MonoBC.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/MonoBC.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#num-clusters-bc).

## Mixed supermodularity of cluster counts for nested wirings

Mixed supermodularity of cluster counts for nested wirings `C ≤ C'`: `k_C(a) + k_C'(b) ≤ k_C(a ⊓
b) + k_C'(a ⊔ b)`.

Formalized by `StatMech.FK.mixed_supermodular_bc`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/MonoBC.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/MonoBC.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#mixed-supermodular-bc).

## Random-cluster weight with a boundary wiring

The unnormalized random-cluster weight with boundary wiring `C`: `edgeProduct G p ω · q ^
numClustersBC G C ω`.

Formalized by `StatMech.FK.bcWeight`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/MonoBC.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/MonoBC.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#bc-weight).

## Partition function with a boundary wiring

The partition function with boundary wiring `C`.

Formalized by `StatMech.FK.bcZ`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/MonoBC.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/MonoBC.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#bc-z).

## Random-cluster probability with a boundary wiring

The random-cluster probability with boundary wiring `C`, `bcWeight / bcZ`.

Formalized by `StatMech.FK.bcProb`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/MonoBC.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/MonoBC.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#bc-prob).

## Holley's condition for weights with nested wirings, $q \ge 1$

Holley's condition for the weights with nested wirings `C ≤ C'` and `q ≥ 1`.

Formalized by `StatMech.FK.bcWeight_cross`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/MonoBC.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/MonoBC.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#bc-weight-cross).

## Holley's condition for probabilities with nested wirings, $q \ge 1$

Holley's condition for the probabilities with nested wirings `C ≤ C'` and `q ≥ 1`.

Formalized by `StatMech.FK.bcProb_cross`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/MonoBC.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/MonoBC.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#bc-prob-cross).

## FKG inequality for the random-cluster measure, $q \ge 1$

FKG inequality for the random-cluster measure (Fortuin, Kasteleyn and Ginibre, 1971): for `q ≥
1` and any boundary wiring `C`, increasing functions are positively correlated under `φ_C`. See
Grimmett, *The Random-Cluster Model* (2006), Chapter 3.

Formalized by `StatMech.FK.bcProb_positively_associated`, a theorem declared in [PhyslibExt/StatisticalMechanics/RandomCluster/MonoBC.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/MonoBC.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#bc-prob-positively-associated).

## Random-cluster comparison of boundary conditions for $q \ge 1$

Comparison of boundary conditions for the random-cluster measure: for `q ≥ 1` and wirings `C ≤
C'`, `φ_C(A) ≤ φ_C'(A)` for every increasing event `A`. This follows from Holley's inequality
(Holley, 1974); see Grimmett, *The Random-Cluster Model* (2006), Chapter 4.

Formalized by `StatMech.FK.bcProb_mono_bc`, a theorem declared in [PhyslibExt/StatisticalMechanics/RandomCluster/MonoBC.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/MonoBC.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#bc-prob-mono-bc).

## Free–wired sandwich for boundary graphs inside the boundary clique

For `q ≥ 1` and `C` inside the boundary clique, `φ^0(A) ≤ φ^C(A) ≤ φ^1(A)` for every increasing
event `A`.

Formalized by `StatMech.FK.bcProb_dlr_sandwich`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/DlrSandwich.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/DlrSandwich.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#bc-prob-dlr-sandwich).

## Sandwich between the free and all-wired boundary conditions

The free lower bound together with the bound by the boundary condition `⊤` (all vertices
wired).

Formalized by `StatMech.FK.bcProb_dlr_sandwich_top`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/DlrSandwich.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/DlrSandwich.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#bc-prob-dlr-sandwich-top).

## Edge marginal of a mass function

The probability `μ(ω(e) = 1)` that the coordinate `e` is open under the mass function `μ`.

Formalized by `StatMech.FK.edgeMargProb`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgeMarginal.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdgeMarginal.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#edge-marg-prob).

## Mass of an event under a mass function

The mass `μ(A)` of an event under the mass function `μ`.

Formalized by `StatMech.FK.eventMassProb`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgeMarginal.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdgeMarginal.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#event-mass-prob).

## Monotone coupling of two mass functions

`P` is a monotone coupling of the mass functions `μ` and `ν`: a nonnegative mass function on
pairs
with marginals `μ` and `ν`, supported on pairs `(ω, ω')` with `ω ≤ ω'`.

Formalized by `StatMech.FK.IsMonotoneCouplingFun`, a structure declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgeMarginal.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdgeMarginal.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#is-monotone-coupling-fun).

## Monotone couplings with equal edge marginals agree on up-sets

Two monotonically coupled measures with the same edge marginals give the same mass to every
increasing event.

Formalized by `StatMech.FK.eventMass_eq_of_edgeMarg_eq`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgeMarginal.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdgeMarginal.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#event-mass-eq-of-edge-marg-eq).

## Event mass under the random-cluster measure with a boundary graph

The mass `φ^C_{G,p,q}(A)` of an event under the random-cluster measure with boundary graph `C`.

Formalized by `StatMech.FK.bcEventMass`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgeMarginal.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdgeMarginal.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#bc-event-mass).

## Boundary-graph comparison $\varphi^{C'}(A) \le q^N \varphi^C(A)$

If the cluster counts with boundary graphs `C ≤ C'` differ by at most `N`, then
`φ^C(A) ≤ q^N φ^{C'}(A)` for nonnegative event indicators.

Formalized by `StatMech.FK.bcEventMass_le_qpow`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgeMarginal.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdgeMarginal.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#bc-event-mass-le-qpow).

## Boundary-supported wirings lie below the boundary clique

A wiring whose edges join boundary vertices lies below the boundary clique.

Formalized by `StatMech.FK.bc_le_boundaryClique`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/IvProperties.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/IvProperties.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#bc-le-boundary-clique).

## Empty wiring gives the free random-cluster measure

The empty wiring gives the free random-cluster measure.

Formalized by `StatMech.FK.bcProb_bot_eq_fkProb`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/IvProperties.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/IvProperties.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#bc-prob-bot-eq-fk-prob).

## Boundary clique gives the wired random-cluster measure

The boundary clique gives the wired random-cluster measure.

Formalized by `StatMech.FK.bcProb_clique_eq_wiredFkProb`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/IvProperties.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/IvProperties.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#bc-prob-clique-eq-wired-fk-prob).

## Boundary wirings lie between free and wired when $q \ge 1$

For `q ≥ 1` and a wiring `C` supported on the boundary, free ≤ `φ_C` ≤ wired on every increasing
event.

Formalized by `StatMech.FK.fkProb_le_bcProb_le_wiredFkProb`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/IvProperties.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/IvProperties.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#fk-prob-le-bc-prob-le-wired-fk-prob).

## Boundary-graph FK measure increases in $p$ for $q \ge 1$

For `q ≥ 1`, the random-cluster measure with boundary graph `C` is increasing in `p` on
increasing events.

Formalized by `StatMech.FK.bcProb_monotone_in_p`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/MonotoneInPBoundaryCondition.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/MonotoneInPBoundaryCondition.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#bc-prob-monotone-in-p).

## Partition function of a conditioning fibre

The partition function of the fibre of `ψ` off `F`: the sum of `bcWeight` over configurations
agreeing with `ψ` off `F`.

Formalized by `StatMech.FK.inducedBcZ`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDominationInner.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDominationInner.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#induced-bc-z).

## Conditional random-cluster measure with a boundary wiring

The random-cluster measure with wiring `C` conditioned on agreeing with `ψ` off the edge set
`F`.

Formalized by `StatMech.FK.condBcProb`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDominationInner.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDominationInner.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#cond-bc-prob).

## Holley's condition for nested-wiring conditional measures, $q \ge 1$

Holley's condition for the conditional measures with nested wirings `C ≤ C'` and `q ≥ 1`.

Formalized by `StatMech.FK.condBcProb_cross`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDominationInner.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDominationInner.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#cond-bc-prob-cross).

## Conditional measures increase with the wiring for $q \ge 1$

For `q ≥ 1` and `C ≤ C'`, the conditional measure with wiring `C` is dominated by the one with
wiring `C'` on increasing events.

Formalized by `StatMech.FK.condBcProb_mono_bc`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDominationInner.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDominationInner.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#cond-bc-prob-mono-bc).

## Disintegration of a boundary-wired measure over conditioning fibres

Disintegration: `φ_C(ω)` is the mass of the fibre of `ω` times the conditional probability of
`ω` in that fibre.

Formalized by `StatMech.FK.bcProb_eq_fibreMass_mul_condBcProb`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDominationInner.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDominationInner.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#bc-prob-eq-fibre-mass-mul-cond-bc-prob).

## Wirings with the boundary clique dominate the wired measure, $q \ge 1$

For `q ≥ 1` the wired measure is dominated by `φ_C'` for any wiring `C'` containing the boundary
clique.

Formalized by `StatMech.FK.wiredFkProb_inner_dominated`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDominationInner.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDominationInner.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#wired-fk-prob-inner-dominated).

## Wired measure conditionally dominated by larger wirings, $q \ge 1$

Conditional version of `wiredFkProb_inner_dominated`.

Formalized by `StatMech.FK.wiredFkProb_inner_dominated_cond`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredDominationInner.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/WiredDominationInner.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html#wired-fk-prob-inner-dominated-cond).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: FKG inequality and monotonicity of random-cluster measures](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/random-cluster-model/fkg-inequality-and-monotonicity-of-random-cluste)
