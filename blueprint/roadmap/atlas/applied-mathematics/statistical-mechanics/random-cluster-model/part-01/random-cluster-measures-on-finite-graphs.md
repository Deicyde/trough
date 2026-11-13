---
declaration: section
origin: cited
lean: StatMech.FK.openSub, StatMech.FK.openSub_eq_inf_fromEdgeSet, StatMech.FK.numClusters, StatMech.FK.edgeProduct, StatMech.FK.fkWeight, StatMech.FK.fkZ, StatMech.FK.fkProb, StatMech.FK.fkPMF
statement: formalized
proof: formalized
---

# Random-cluster measures on finite graphs

77 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html).

## Open subgraph of an edge configuration

The open subgraph of `G` under the edge configuration `ω`: the edges of `G` that `ω`
declares open.

Formalized by `StatMech.FK.openSub`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/RandomCluster.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/RandomCluster.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#open-sub).

## Open subgraph as the meet of $G$ with the open-edge graph

The open subgraph is `G ⊓ fromEdgeSet {e | ω e = true}` in Mathlib's terms.

Formalized by `StatMech.FK.openSub_eq_inf_fromEdgeSet`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/RandomCluster.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/RandomCluster.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#open-sub-eq-inf-from-edge-set).

## Number of open clusters

The number `k(ω)` of open clusters: connected components of the open subgraph, isolated
vertices included.

Formalized by `StatMech.FK.numClusters`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/RandomCluster.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/RandomCluster.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#num-clusters).

## Bernoulli edge product

The Bernoulli edge product `∏_{e ∈ E(G)} (p if e open, 1 - p if e closed)`.

Formalized by `StatMech.FK.edgeProduct`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/RandomCluster.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/RandomCluster.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#edge-product).

## Unnormalized random-cluster weight

The unnormalized random-cluster weight `p ^ o(ω) (1 - p) ^ c(ω) q ^ k(ω)`.

Formalized by `StatMech.FK.fkWeight`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/RandomCluster.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/RandomCluster.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#fk-weight).

## Ambient FK normalizer

The ambient FK normalizer, summing over every bit assignment on `Sym2 V`.
Each loop or nonedge contributes a factor of two relative to the edge partition function
`ecz_fkZEdge` defined in `EdgePartitionFunction`.

Formalized by `StatMech.FK.fkZ`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/RandomCluster.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/RandomCluster.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#fk-z).

## Probability of an ambient FK configuration

The probability of an ambient configuration: `fkWeight G p q ω / fkZ G p q`.
For `0 < p < 1` and `q > 0`, its graph-edge marginal is the random-cluster law and
unused coordinates are uniform.

Formalized by `StatMech.FK.fkProb`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/RandomCluster.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/RandomCluster.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#fk-prob).

## Ambient random-cluster law as a probability mass function

The ambient extension of the random-cluster edge law as a `PMF` on all `Sym2 V`
configurations, with independent uniform bits on loops and nonedges.

Formalized by `StatMech.FK.fkPMF`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/RandomCluster.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/RandomCluster.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#fk-pmf).

## At $q = 1$ the random-cluster weight is the Bernoulli product

At `q = 1` the random-cluster weight is the Bernoulli product weight.

Formalized by `StatMech.FK.fkWeight_one`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/RandomCluster.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/RandomCluster.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#fk-weight-one).

## Agreement of configurations off an edge set

`ω` agrees with `ψ` on every edge outside `F`.

Formalized by `StatMech.FK.AgreesOff`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/DomainMarkov.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/DomainMarkov.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#agrees-off).

## Fibre of configurations agreeing off an edge set

The fibre of configurations agreeing with `ψ` off `F`.

Formalized by `StatMech.FK.condFibre`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/DomainMarkov.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/DomainMarkov.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#cond-fibre).

## Total FK weight of a fibre

The total FK weight of the fibre `condFibre F ψ`.

Formalized by `StatMech.FK.inducedFkZ`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/DomainMarkov.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/DomainMarkov.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#induced-fk-z).

## FK measure induced on a fibre

The FK measure induced on the fibre `condFibre F ψ`: FK weight divided by the fibre's total
weight.

Formalized by `StatMech.FK.inducedFkProb`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/DomainMarkov.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/DomainMarkov.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#induced-fk-prob).

## Random-cluster measure conditioned on the edges off a set

The random-cluster measure conditioned on agreeing with `ψ` off `F`.

Formalized by `StatMech.FK.condFkProb`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/DomainMarkov.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/DomainMarkov.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#cond-fk-prob).

## Domain Markov property (finite volume)

Conditioned on the states of the edges outside `F`,
the random-cluster measure is the FK weight renormalized on the fibre
(Grimmett, *The Random-Cluster Model*, 2006, Lemma 4.13).

Formalized by `StatMech.FK.condFkProb_eq_inducedFkProb`, a theorem declared in [PhyslibExt/StatisticalMechanics/RandomCluster/DomainMarkov.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/DomainMarkov.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#cond-fk-prob-eq-induced-fk-prob).

## Closing the edges of a set in a configuration

The configuration that closes every edge of `F` and agrees with `ψ` elsewhere.

Formalized by `StatMech.FK.projOff`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FKDisjointBoxDomainMarkov.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FKDisjointBoxDomainMarkov.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#proj-off).

## Fibre representatives with every edge of a set closed

Representatives of the fibres of `F`: configurations with every edge of `F` closed.

Formalized by `StatMech.FK.fibreReps`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FKDisjointBoxDomainMarkov.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FKDisjointBoxDomainMarkov.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#fibre-reps).

## Event depending only on edges outside a set

Membership in `B` depends only on the states of edges outside `F`.

Formalized by `StatMech.FK.DependsOnOutside`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FKDisjointBoxDomainMarkov.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FKDisjointBoxDomainMarkov.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#depends-on-outside).

## Toggling a non-edge leaves the open subgraph unchanged

Off the edges of `G`, flipping `e` does not change the open subgraph.

Formalized by `StatMech.FK.openSub_setOpen_eq_setClosed_of_notMem`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FiniteEnergy.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FiniteEnergy.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#open-sub-set-open-eq-set-closed-of-not-m).

## Opening an edge does not increase the cluster count

Opening an edge does not increase the number of clusters. This is a special case of
Mathlib's `SimpleGraph.ConnectedComponent.card_le_card_of_le`, which proves it.

Formalized by `StatMech.FK.numClusters_setOpen_le`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FiniteEnergy.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FiniteEnergy.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#num-clusters-set-open-le).

## Opening an edge lowers the cluster count by at most one

Opening an edge lowers the number of clusters by at most one.

Formalized by `StatMech.FK.numClusters_setClosed_le_setOpen_succ`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FiniteEnergy.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FiniteEnergy.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#num-clusters-set-closed-le-set-open-succ).

## Bernoulli product over the edges other than one edge

The Bernoulli product over the edges of `G` other than `e`.

Formalized by `StatMech.FK.edgeRest`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FiniteEnergy.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FiniteEnergy.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#edge-rest).

## Conditional probability that an edge is open given the rest

The conditional probability under `φ_{G,p,q}` that `e` is open given the states of all
other edges: `φ(setOpen e ω) / (φ(setOpen e ω) + φ(setClosed e ω))`.

Formalized by `StatMech.FK.condOpen`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FiniteEnergy.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FiniteEnergy.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#cond-open).

## Finite-energy constant of the random-cluster measure

The finite-energy constant `min (p / (p + q (1 - p))) (1 - p)`.

Formalized by `StatMech.FK.cFE`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FiniteEnergy.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FiniteEnergy.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#c-fe).

## Finite-energy property

**Finite-energy property** of the random-cluster measure. For `p ∈ (0, 1)` and `q ≥ 1`, the
conditional probability that an edge is open given all other edges lies in
`[cFE p q, 1 - cFE p q]`. For edges of `G` the sharper bounds `p / (p + q (1 - p))` and `p` are
proved along the way. See G. Grimmett, *The Random-Cluster Model* (2006), Chapter 3.

Formalized by `StatMech.FK.finite_energy`, a theorem declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FiniteEnergy.lean, line 313](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FiniteEnergy.lean#L313). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#finite-energy).

## Inhomogeneous Bernoulli edge product

The inhomogeneous Bernoulli product `∏_{e ∈ E(G)} (pf e if e open, 1 - pf e if closed)`.

Formalized by `StatMech.FK.edgeProductW`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/RussoDerivativeBeta.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/RussoDerivativeBeta.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#edge-product-w).

## Inhomogeneous random-cluster weight

The inhomogeneous random-cluster weight `edgeProductW G pf ω · q ^ k(ω)`.

Formalized by `StatMech.FK.fkWeightW`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/RussoDerivativeBeta.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/RussoDerivativeBeta.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#fk-weight-w).

## Partition function of the inhomogeneous random-cluster measure

The partition function of the inhomogeneous random-cluster measure.

Formalized by `StatMech.FK.fkZW`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/RussoDerivativeBeta.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/RussoDerivativeBeta.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#fk-zw).

## Inhomogeneous random-cluster probability

The inhomogeneous random-cluster probability `fkWeightW / fkZW`.

Formalized by `StatMech.FK.fkProbW`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/RussoDerivativeBeta.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/RussoDerivativeBeta.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#fk-prob-w).

## Expectation under the inhomogeneous random-cluster measure

The expectation of `g` under the inhomogeneous random-cluster measure.

Formalized by `StatMech.FK.fkMeanW`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/RussoDerivativeBeta.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/RussoDerivativeBeta.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#fk-mean-w).

## Covariance under the inhomogeneous random-cluster measure

The covariance `E[f g] - E[f] E[g]` under the inhomogeneous random-cluster measure
(a finite form of Mathlib's `ProbabilityTheory.covariance`).

Formalized by `StatMech.FK.fkCovW`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/RussoDerivativeBeta.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/RussoDerivativeBeta.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#fk-cov-w).

## Real-valued indicator that an edge is open

The real-valued state `𝟙[e open]` of the edge `e`.

Formalized by `StatMech.FK.coordR`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/RussoDerivativeBeta.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/RussoDerivativeBeta.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#coord-r).

## Inhomogeneous Bernoulli product over all edges but one

The inhomogeneous Bernoulli product over the edges of `G` other than `e₀`.

Formalized by `StatMech.FK.edgeProductWOff`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/RussoDerivativeBeta.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/RussoDerivativeBeta.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#edge-product-woff).

## Unnormalized inhomogeneous random-cluster expectation

The unnormalized expectation `∑_ω g(ω) fkWeightW G pf q ω`.

Formalized by `StatMech.FK.fkNumerW`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/RussoDerivativeBeta.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/RussoDerivativeBeta.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#fk-numer-w).

## Differential formula

**Differential formula** for the random-cluster measure: the derivative of `φ[g]` in the
parameter of the edge `e₀` is `Cov(g, 𝟙[e₀ open]) / (p (1 - p))` with `p = pf e₀`. See
G. Grimmett, *The Random-Cluster Model* (2006), Chapter 3.

Formalized by `StatMech.FK.hasDerivAt_fkMeanW`, a theorem declared in [PhyslibExt/StatisticalMechanics/RandomCluster/RussoDerivativeBeta.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/RussoDerivativeBeta.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#has-deriv-at-fk-mean-w).

## Probability of an event under the inhomogeneous random-cluster measure

The probability of the event `A` under the inhomogeneous random-cluster measure.

Formalized by `StatMech.FK.fkProbWOf`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/RussoDerivativeBeta.lean, line 371](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/RussoDerivativeBeta.lean#L371). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#fk-prob-wof).

## Derivative in $\beta$ of the edge parameter $1 - e^{-\beta J}$

The derivative of the edge parameter `p(β) = 1 - exp (-β J)` is `J exp (-β J)`.

Formalized by `StatMech.FK.hasDerivAt_paramOfBeta`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/RussoDerivativeBeta.lean, line 401](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/RussoDerivativeBeta.lean#L401). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#has-deriv-at-param-of-beta).

## Edge parameters $p_e(\beta) = 1 - e^{-\beta J_e}$

The edge parameters `p_e(β) = 1 - exp (-β J_e)`.

Formalized by `StatMech.FK.betaParams`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/RussoDerivativeBetaSum.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/RussoDerivativeBetaSum.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#beta-params).

## Logarithmic $\beta$-derivative of the random-cluster weight

The logarithmic `β`-derivative of the random-cluster weight under `betaParams`:
`∑_{e ∈ E(G)} (J_e / p_e) (𝟙[e open] - p_e)`.

Formalized by `StatMech.FK.betaScore`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/RussoDerivativeBetaSum.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/RussoDerivativeBetaSum.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#beta-score).

## Differential formula in `β`

**Differential formula in `β`** for the random-cluster measure with edge parameters
`1 - exp (-β J_e)`: `d/dβ φ_β[g] = ∑_e (J_e / p_e) Cov(g, 𝟙[e open])`. See G. Grimmett,
*The Random-Cluster Model* (2006), Chapter 3.

Formalized by `StatMech.FK.hasDerivAt_fkMeanW_beta_sum`, a theorem declared in [PhyslibExt/StatisticalMechanics/RandomCluster/RussoDerivativeBetaSum.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/RussoDerivativeBetaSum.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#has-deriv-at-fk-mean-w-beta-sum).

## Number of open edges

The number `o(ω)` of open edges of `G` in `ω`.

Formalized by `StatMech.FK.openCount`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/Tilt.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/Tilt.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#open-count).

## Number of closed edges

The number `c(ω)` of closed edges of `G` in `ω`.

Formalized by `StatMech.FK.closedCount`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/Tilt.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/Tilt.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#closed-count).

## Tilt factor between two edge parameters

The tilt factor `λ = p₂ (1 - p₁) / ((1 - p₂) p₁)`, the ratio of the odds of an open edge
at `p₂` and at `p₁`.

Formalized by `StatMech.FK.tiltFactor`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/Tilt.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/Tilt.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#tilt-factor).

## Random-cluster expectation of an observable

The expectation `φ_{G,p,q}[X] = ∑_ω φ_{G,p,q}(ω) X(ω)` of an observable `X`.

Formalized by `StatMech.FK.fkExpect`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/Tilt.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/Tilt.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#fk-expect).

## Relabelling of an edge configuration by a vertex permutation

The configuration `ω ∘ σ` on edges: the edge `e` is open in `reCfg σ ω` iff `σ e` is open in
`ω`. See also `reCfgIso`, the same relabelling along an equivalence `V ≃ W`.

Formalized by `StatMech.FK.reCfg`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvariance.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvariance.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#re-cfg).

## Relabelling as a permutation of the configuration space

Relabelling by `σ` as a permutation of the configuration space, with inverse relabelling
by `σ⁻¹`.

Formalized by `StatMech.FK.reCfgEquiv`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvariance.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvariance.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#re-cfg-equiv).

## Automorphism as an isomorphism of open subgraphs

An automorphism `σ` of `G` is a graph isomorphism from the open subgraph of the relabelled
configuration `reCfg σ ω` to the open subgraph of `ω`.

Formalized by `StatMech.FK.fkTI_openSubIso`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvariance.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvariance.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#fk-ti-open-sub-iso).

## Graph automorphisms preserve the free FK probability

Graph automorphisms preserve the free FK probability. See also `fvs_fkProb_reCfgIso` for
isomorphisms between two graphs.

Formalized by `StatMech.FK.fkTI_fkProb_reCfg`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvariance.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvariance.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#fk-ti-fk-prob-re-cfg).

## Boundary-preserving automorphism as an isomorphism of wired graphs

An automorphism `σ` of `G` preserving the boundary set is a graph isomorphism between the
wired graphs (open edges plus all boundary pairs) of `reCfg σ ω` and `ω`.

Formalized by `StatMech.FK.fkTI_wiredGraphIso`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvariance.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvariance.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#fk-ti-wired-graph-iso).

## Boundary-preserving automorphisms preserve the wired FK probability

Graph automorphisms preserving the boundary preserve the wired FK probability.

Formalized by `StatMech.FK.fkTI_wiredFkProb_reCfg`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvariance.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvariance.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#fk-ti-wired-fk-prob-re-cfg).

## Graph automorphisms preserve free FK edge marginals

Under the free FK measure, the edges `e` and `σ e` are open with the same probability.

Formalized by `StatMech.FK.fkTI_edgeMargProb_fkProb_reCfg`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvariance.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvariance.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#fk-ti-edge-marg-prob-fk-prob-re-cfg).

## Boundary-preserving automorphisms preserve wired FK edge marginals

Under the wired FK measure, the edges `e` and `σ e` are open with the same probability.

Formalized by `StatMech.FK.fkTI_edgeMargProb_wiredFkProb_reCfg`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvariance.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvariance.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#fk-ti-edge-marg-prob-wired-fk-prob-re-cf).

## Box symmetry of $\mathbb{Z}^d$

A symmetry of `ℤ^d` that preserves nearest-neighbour adjacency and every centered box
`Λ_n = [-n, n]^d`, such as a coordinate reflection or a coordinate permutation.

Formalized by `StatMech.FK.BoxSym`, a structure declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvariance.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvariance.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#box-sym).

## Restriction of a box symmetry to a box

The restriction of a box symmetry to a permutation of the vertices of the box `Λ_n`.

Formalized by `StatMech.FK.BoxSym.lift`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvariance.lean, line 290](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvariance.lean#L290). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#lift).

## Box symmetries preserve the wired $q = 2$ density of box edges

Box symmetries preserve the wired `q = 2` infinite-volume edge density. See also
`rot_wired_density_boxSym` for the statement on edges of `ℤ^d`.

Formalized by `StatMech.FK.fkTI_wired_density_shift_inv`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvariance.lean, line 342](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvariance.lean#L342). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#fk-ti-wired-density-shift-inv).

## Box symmetries preserve the free $q = 2$ density of box edges

Box symmetries preserve the free `q = 2` infinite-volume edge density. See also
`rot_free_density_boxSym` for the statement on edges of `ℤ^d`.

Formalized by `StatMech.FK.fkTI_free_density_shift_inv`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvariance.lean, line 355](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvariance.lean#L355). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#fk-ti-free-density-shift-inv).

## Reflection of $\mathbb{Z}^d$ in one coordinate

The reflection `x ↦ x` with the `j`-th coordinate negated.

Formalized by `StatMech.FK.fkTI_signFlipEquiv`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvariance.lean, line 371](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvariance.lean#L371). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#fk-ti-sign-flip-equiv).

## Coordinate reflection as a box symmetry

The reflection in the `j`-th coordinate as a box symmetry.

Formalized by `StatMech.FK.fkTI_signFlip`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvariance.lean, line 378](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvariance.lean#L378). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#fk-ti-sign-flip).

## Pull-back of an edge configuration along a vertex bijection

The pull-back of a configuration `ω` on the edges of `W` along `σ : V ≃ W`: the edge `e` is
open in `reCfgIso σ ω` iff `σ e` is open in `ω`. For `V = W` it is `reCfg`
(`fvs_reCfgIso_eq_reCfg`).

Formalized by `StatMech.FK.reCfgIso`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FiniteVolumeShift.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FiniteVolumeShift.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#re-cfg-iso).

## Pull-back of configurations as an equivalence

Pull-back along `σ` as an equivalence of configuration spaces, with inverse the pull-back
along `σ⁻¹`.

Formalized by `StatMech.FK.reCfgIsoEquiv`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FiniteVolumeShift.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FiniteVolumeShift.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#re-cfg-iso-equiv).

## Pull-back along a permutation is relabelling

For a permutation `σ` of `V`, pulling back along `σ` is the relabelling `reCfg σ`.

Formalized by `StatMech.FK.fvs_reCfgIso_eq_reCfg`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FiniteVolumeShift.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FiniteVolumeShift.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#fvs-re-cfg-iso-eq-re-cfg).

## Open-subgraph isomorphism for a pulled-back configuration

An isomorphism `σ : G ≃ H` is a graph isomorphism from the open subgraph of the pulled-back
configuration `reCfgIso σ ω` to the open subgraph of `ω`.

Formalized by `StatMech.FK.fvs_openSubIso`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FiniteVolumeShift.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FiniteVolumeShift.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#fvs-open-sub-iso).

## Isomorphic graphs have equal free FK probabilities after relabelling

Isomorphic graphs have the same free FK probability, up to relabelling by the isomorphism.
See also `fkTI_fkProb_reCfg`, the special case of an automorphism.

Formalized by `StatMech.FK.fvs_fkProb_reCfgIso`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FiniteVolumeShift.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FiniteVolumeShift.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#fvs-fk-prob-re-cfg-iso).

## Wired-graph isomorphism for a pulled-back configuration

An isomorphism `σ : G ≃ H` matching the boundary sets is a graph isomorphism between the
wired graphs of `reCfgIso σ ω` and `ω`.

Formalized by `StatMech.FK.fvs_wiredGraphIso`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FiniteVolumeShift.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FiniteVolumeShift.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#fvs-wired-graph-iso).

## Boundary-matching isomorphisms preserve wired FK probabilities

Isomorphic graphs with matching boundary sets have the same wired FK probability, up to
relabelling. See also `fkTI_wiredFkProb_reCfg`.

Formalized by `StatMech.FK.fvs_wiredFkProb_reCfgIso`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FiniteVolumeShift.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FiniteVolumeShift.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#fvs-wired-fk-prob-re-cfg-iso).

## Boundary-matching isomorphisms transport FK edge marginals

Graph isomorphisms transport the wired and the free FK edge marginals: `σ e` is open in `H`
with the same probability as `e` in `G`.

Formalized by `StatMech.FK.fvs_finiteVolume_shift_invariant`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FiniteVolumeShift.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FiniteVolumeShift.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#fvs-finite-volume-shift-invariant).

## Translated box in $\mathbb{Z}^d$

The translated box `v + Λ_m = {y ∈ ℤ^d : ‖y - v‖_∞ ≤ m}`.

Formalized by `StatMech.FK.fvs_transBox`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FiniteVolumeShift.lean, line 304](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FiniteVolumeShift.lean#L304). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#fvs-trans-box).

## Vertex type of a translated box

The vertices of the translated box `v + Λ_m`, as a subtype of `ℤ^d`.

Formalized by `StatMech.FK.fvs_transBoxVerts`, an abbreviation declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FiniteVolumeShift.lean, line 307](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FiniteVolumeShift.lean#L307). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#fvs-trans-box-verts).

## Translation from the centered box onto a translated box

The translation `x ↦ x + v` from the centered box `Λ_m` onto `v + Λ_m`.

Formalized by `StatMech.FK.fvs_transEquiv`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FiniteVolumeShift.lean, line 311](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FiniteVolumeShift.lean#L311). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#fvs-trans-equiv).

## Nearest-neighbour graph on a translated box

The nearest-neighbour graph of `ℤ^d` restricted to `v + Λ_m`.

Formalized by `StatMech.FK.fvs_transBoxGraph`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FiniteVolumeShift.lean, line 334](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FiniteVolumeShift.lean#L334). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#fvs-trans-box-graph).

## Vertex boundary of a translated box

The vertex boundary of `v + Λ_m`: the translate of the vertex boundary of `Λ_m`.

Formalized by `StatMech.FK.fvs_transBoxBoundary`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FiniteVolumeShift.lean, line 343](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FiniteVolumeShift.lean#L343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#fvs-trans-box-boundary).

## Translation covariance of FK edge marginals on boxes

The wired and free FK edge marginals on the translated box `v + Λ_m` are the marginals on the
centered box `Λ_m`, transported by `x ↦ x + v`.

Formalized by `StatMech.FK.fvs_box_translation_edgeMarg`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FiniteVolumeShift.lean, line 373](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FiniteVolumeShift.lean#L373). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#fvs-box-translation-edge-marg).

## Some translated box leaves the centered box for $d \ge 1$

For `d ≥ 1`, some translated box `v + Λ_m` is not contained in `Λ_m`, so translation is not a
box symmetry in the sense of `BoxSym`.

Formalized by `StatMech.FK.fvs_transBox_ne_box`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FiniteVolumeShift.lean, line 386](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FiniteVolumeShift.lean#L386). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#fvs-trans-box-ne-box).

## Monotonicity of the open subgraph in the configuration

The open subgraph is monotone in the configuration. The same statement is
`StatMech.Sharpness.openSub_mono` in `BkCriterion`.

Formalized by `StatMech.FK.openSub_mono`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TwoPoint.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TwoPoint.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#open-sub-mono).

## Event that two vertices are joined by open edges

The event that `x` and `y` are joined by a path of open edges of `G`.

Formalized by `StatMech.FK.connEvent`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TwoPoint.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TwoPoint.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#conn-event).

## Two-point function of the free random-cluster measure

The two-point function of the free random-cluster measure on a finite graph: the probability
`φ(x ↔ y)` that `x` and `y` are connected by open edges.

Formalized by `StatMech.FK.twoPointFun`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TwoPoint.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TwoPoint.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#two-point-fun).

## FKG inequality for connection events for $q \ge 1$

FKG for connection events: for `q ≥ 1`, `φ(x ↔ y) φ(u ↔ v) ≤ φ(x ↔ y, u ↔ v)`.

Formalized by `StatMech.FK.twoPointFun_fkg`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TwoPoint.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TwoPoint.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html#two-point-fun-fkg).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Random-cluster measures on finite graphs](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/random-cluster-model/random-cluster-measures-on-finite-graphs)
