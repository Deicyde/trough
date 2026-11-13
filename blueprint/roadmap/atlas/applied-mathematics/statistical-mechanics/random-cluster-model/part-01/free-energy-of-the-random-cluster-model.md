---
declaration: section
origin: cited
lean: StatMech.FK.bxt_ambientNegLogZ, StatMech.FK.bxt_E, StatMech.FK.bxt_NegLogDoublingBound, StatMech.FK.fis_interface, StatMech.FK.fis_CrossInterface, StatMech.FK.agl_left, StatMech.FK.agl_right, StatMech.FK.agl_sumEquiv
statement: formalized
proof: formalized
---

# Free energy of the random-cluster model

105 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html).

## Negative log ambient normalizer of the box $\Lambda_n$

The negative log ambient normalizer `-log (fkZ Λ_n (logistic t) 2)` of the box `Λ_n`.

Formalized by `StatMech.FK.bxt_ambientNegLogZ`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxTiling.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/BoxTiling.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#bxt-ambient-neg-log-z).

## Edge count of the box $\Lambda_n$

The number of edges of the box `Λ_n`.

Formalized by `StatMech.FK.bxt_E`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxTiling.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/BoxTiling.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#bxt-e).

## Doubling bound at the dyadic scales $2^j$

Doubling bound at the dyadic scales: `u(2^{j+1}) ≤ 2^d u(2^j) + I_j (-log(1 - p))` with
`|2^d E(2^j) - E(2^{j+1})| ≤ I_j` and `∑_j I_j / E(2^{j+1}) < ∞`.

Formalized by `StatMech.FK.bxt_NegLogDoublingBound`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxTiling.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/BoxTiling.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#bxt-neg-log-doubling-bound).

## Interface edges of a graph on a disjoint union

The interface edges of `K`: edges not in the disjoint union `G ⊕ H`.

Formalized by `StatMech.FK.fis_interface`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FKInterfaceSubadd.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FKInterfaceSubadd.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#fis-interface).

## Graph glued from two graphs along an interface

`K` contains `G ⊕ H` and adds no edges inside `V` or inside `W`; all extra edges join `V` to
`W`.

Formalized by `StatMech.FK.fis_CrossInterface`, a structure declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FKInterfaceSubadd.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FKInterfaceSubadd.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#fis-cross-interface).

## Graph induced on the vertices satisfying a predicate

The graph induced by `K₀` on `{x | P x}`.

Formalized by `StatMech.FK.agl_left`, an abbreviation declared in [PhyslibExt/StatisticalMechanics/RandomCluster/AdditiveGluing.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/AdditiveGluing.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#agl-left).

## Graph induced on the vertices failing a predicate

The graph induced by `K₀` on `{x | ¬ P x}`.

Formalized by `StatMech.FK.agl_right`, an abbreviation declared in [PhyslibExt/StatisticalMechanics/RandomCluster/AdditiveGluing.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/AdditiveGluing.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#agl-right).

## Vertex set as a disjoint sum of a subset and its complement

The identification `{P} ⊕ {¬P} ≃ U`.

Formalized by `StatMech.FK.agl_sumEquiv`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/AdditiveGluing.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/AdditiveGluing.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#agl-sum-equiv).

## Graph transported to the sum of a subset and its complement

`K₀` transported to `{P} ⊕ {¬P}`.

Formalized by `StatMech.FK.agl_glueGraph`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/AdditiveGluing.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/AdditiveGluing.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#agl-glue-graph).

## Isomorphism between a graph and its transported copy

`K₀` is isomorphic to its transport `agl_glueGraph`.

Formalized by `StatMech.FK.agl_iso`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/AdditiveGluing.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/AdditiveGluing.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#agl-iso).

## Number of edges between a vertex subset and its complement

The number of edges of `K₀` joining `{P}` to `{¬P}`.

Formalized by `StatMech.FK.agl_interfaceCard`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/AdditiveGluing.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/AdditiveGluing.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#agl-interface-card).

## Isomorphism of translated induced lattice graphs

Translating vertex embeddings by `v` gives isomorphic induced lattice graphs.

Formalized by `StatMech.FK.agl_transBlockIso`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/AdditiveGluing.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/AdditiveGluing.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#agl-trans-block-iso).

## Isomorphism of a box with its translated copy in the predicate part

A translated copy of `Λ_m` inside `{P}` induces a graph isomorphic to `Λ_m`.

Formalized by `StatMech.FK.agl_leftBlockIso`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/AdditiveGluing.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/AdditiveGluing.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#agl-left-block-iso).

## Isomorphism of a box with its translated copy in the complement part

A translated copy of `Λ_m` inside `{¬P}` induces a graph isomorphic to `Λ_m`.

Formalized by `StatMech.FK.agl_rightBlockIso`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/AdditiveGluing.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/AdditiveGluing.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#agl-right-block-iso).

## Scales $K_j = 2^{j+1} - 1$

The scales `K_j = 2^{j+1} - 1`, with `K_0 = 1` and `K_{j+1} = 2 K_j + 1`.

Formalized by `StatMech.FK.agl_K`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/AdditiveGluing.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/AdditiveGluing.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#agl-k).

## Negative log ambient normalizer of a box

The negative log ambient normalizer of `Λ_n`; the same as `bxt_ambientNegLogZ`.

Formalized by `StatMech.FK.agl_ambientNegLogZ`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/AdditiveGluing.lean, line 307](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/AdditiveGluing.lean#L307). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#agl-ambient-neg-log-z).

## Number of edges of a box

The number of edges of `Λ_n`; the same as `bxt_E`.

Formalized by `StatMech.FK.agl_E`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/AdditiveGluing.lean, line 311](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/AdditiveGluing.lean#L311). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#agl-e).

## Additive doubling bound along the scales $K_j$

Doubling bound along the scales `K_j`: `u(K_{j+1}) ≤ 2^d u(K_j) + I_j (-log(1 - p))` with
`|2^d E(K_j) - E(K_{j+1})| ≤ I_j` and `∑_j I_j / E(K_{j+1}) < ∞`.

Formalized by `StatMech.FK.agl_AdditiveDoublingBound`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/AdditiveGluing.lean, line 322](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/AdditiveGluing.lean#L322). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#agl-additive-doubling-bound).

## Assumed doubling, boundedness and oscillation data along $K_j$

The doubling bound along `K_j`, a uniform bound on the ambient per-edge values
`agl_ambientNegLogZ / agl_E` at those scales, and vanishing oscillation of `ivp2_ambientTiltLogZ`
between `Λ_n` and `Λ_{K_{b(n)}}`. These are assumptions, not a box-convergence result.

Formalized by `StatMech.FK.agl_AdditiveBoxFeketeData`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/AdditiveGluing.lean, line 434](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/AdditiveGluing.lean#L434). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#agl-additive-box-fekete-data).

## Fekete's lemma with a general normalization

Fekete's lemma normalized by `e n` instead of `n`: if `u` is subadditive with `u n / n`
bounded below and `e n / n → c ≠ 0`, then `u n / e n → lim / c`. Built on Mathlib's
`Subadditive.tendsto_lim`.

Formalized by `StatMech.FK.fkl_tendsto_div_of_subadditive`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FeketeLimit.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FeketeLimit.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#fkl-tendsto-div-of-subadditive).

## Hypotheses of the normalized Fekete lemma are satisfiable

The hypotheses of `fkl_tendsto_div_of_subadditive` hold together for `u = 0`, `e n = n`.

Formalized by `StatMech.FK.fkl_superMultiplicative_satisfiable`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FeketeLimit.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FeketeLimit.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#fkl-super-multiplicative-satisfiable).

## Dyadic convergence data for the ambient tilted log normalizer

The ambient tilted log normalizer of `Λ_{2^j}` is increasing in `j` up to summable defects and
  bounded
above, and
the ambient tilted log normalizer of `Λ_n` differs from that of the dyadic box below it by a
  vanishing
oscillation.

Formalized by `StatMech.FK.bpv_AmbientTiltLogZConvergenceData`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeEnergyDyadic.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FreeEnergyDyadic.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#bpv-ambient-tilt-log-zconvergence-data).

## Fekete's lemma with a sublinear correction

Fekete's lemma with an `o(n)` correction: if `u n + c n` is subadditive and bounded below after
dividing by `n`, and `c n / n → 0`, then `u n / n` converges. See also Mathlib's
`Subadditive.tendsto_lim`.

Formalized by `StatMech.FK.bfd_tendsto_div_of_nearSubadditive`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeEnergyNearSubadditive.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FreeEnergyNearSubadditive.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#bfd-tendsto-div-of-near-subadditive).

## Components of a disjoint union sent to components of the summands

The map sending a component of `G ⊕g H` to the corresponding component of `G` or `H`.

Formalized by `StatMech.FK.fsm_ccToSum`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/SuperMultiplicative.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/SuperMultiplicative.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#fsm-cc-to-sum).

## Inclusion of summand components into a disjoint union

The inclusion of the components of `G` and of `H` into those of `G ⊕g H`.

Formalized by `StatMech.FK.fsm_sumToCC`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/SuperMultiplicative.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/SuperMultiplicative.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#fsm-sum-to-cc).

## Connected components of a disjoint union of graphs

The connected components of `G ⊕g H` are those of `G` and those of `H`.

Formalized by `StatMech.FK.fsm_ccSumEquiv`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/SuperMultiplicative.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/SuperMultiplicative.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#fsm-cc-sum-equiv).

## Gluing edge configurations on a disjoint union

Gluing edge configurations: `σ` on edges inside `V`, `τ` on edges inside `W`, and closed on
pairs joining `V` to `W`.

Formalized by `StatMech.FK.fsm_combine`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/SuperMultiplicative.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/SuperMultiplicative.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#fsm-combine).

## Ambient FK normalizer is supermultiplicative under disjoint union

The ambient FK normalizer is supermultiplicative under disjoint union:
`Z_G Z_H ≤ Z_{G ⊕g H}`. Each `Z` sums over all `Sym2` configurations.

Formalized by `StatMech.FK.fsm_fkZ_sum_ge`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/SuperMultiplicative.lean, line 382](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/SuperMultiplicative.lean#L382). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#fsm-fk-z-sum-ge).

## Bijection of unordered pairs induced by a bijection

The equivalence `Sym2 V ≃ Sym2 W` induced by `V ≃ W`.

Formalized by `StatMech.FK.fsm_sym2Congr`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/SuperMultiplicative.lean, line 430](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/SuperMultiplicative.lean#L430). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#fsm-sym2-congr).

## Graph isomorphism restricted to open subgraphs

A graph isomorphism `G ≃g H` restricts to an isomorphism of open subgraphs, with the
configuration on `G` pulled back from `H`.

Formalized by `StatMech.FK.fsm_openSubIso`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/SuperMultiplicative.lean, line 438](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/SuperMultiplicative.lean#L438). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#fsm-open-sub-iso).

## Isomorphism invariance of the ambient FK normalizer

The ambient FK normalizer is invariant under graph isomorphism.

Formalized by `StatMech.FK.fsm_fkZ_iso`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/SuperMultiplicative.lean, line 483](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/SuperMultiplicative.lean#L483). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#fsm-fk-z-iso).

## Subadditivity of $-\log Z$ along a juxtaposition sequence

Along a sequence with `G_{m+n} ≅ G_m ⊕g G_n`, the sequence `-log Z_{G_n}` is subadditive.

Formalized by `StatMech.FK.fsm_subadditive_neglog_fkZ`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/SuperMultiplicative.lean, line 515](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/SuperMultiplicative.lean#L515). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#fsm-subadditive-neglog-fk-z).

## Edgeless graphs satisfy the juxtaposition hypothesis

Edgeless graphs on `Fin n` satisfy the juxtaposition hypothesis `G_{m+n} ≅ G_m ⊕g G_n`.

Formalized by `StatMech.FK.fsm_juxtaposition_satisfiable`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/SuperMultiplicative.lean, line 526](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/SuperMultiplicative.lean#L526). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#fsm-juxtaposition-satisfiable).

## Isomorphism of induced graphs from injections with equal range

Graphs induced on `K₀` by two injections with the same range are isomorphic.

Formalized by `StatMech.FK.qp_comapIsoOfRangeEq`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-comap-iso-of-range-eq).

## Induced graphs with equal range have equal FK partition functions

Graphs induced by two injections with the same range have the same FK partition function.

Formalized by `StatMech.FK.qp_fkZ_comap_range`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-fk-z-comap-range).

## FK partition function at least the all-closed weight for $q \ge 1$

For `q ≥ 1`, the FK partition function is at least the weight `(1 - p)^{|E|}` of the all-
closed configuration.

Formalized by `StatMech.FK.qp_fkZ_ge_allClosed`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-fk-z-ge-all-closed).

## Bound $-\log Z \le |E|\,(-\log(1-p))$ for $q \ge 1$

For `q ≥ 1`, `-log Z ≤ |E| · (-log (1 - p))`.

Formalized by `StatMech.FK.qp_neglogZ_le_edges`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-neglog-z-le-edges).

## Graph induced on vertices with tags in $S$

The graph induced on the vertices whose tag lies in `S`.

Formalized by `StatMech.FK.qp_restG`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-rest-g).

## Block of a tag: graph induced on its vertices

The block of tag `τ`: the graph induced on the vertices with tag `τ`.

Formalized by `StatMech.FK.qp_blkG`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-blk-g).

## Straddling of a predicate by an edge

An edge straddles `P` if exactly one endpoint satisfies `P`.

Formalized by `StatMech.FK.qp_straddleP`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-straddle-p).

## Set of edges straddling a predicate

The edges of `K₀` that straddle `P`.

Formalized by `StatMech.FK.qp_straddleEdges`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-straddle-edges).

## Isomorphism of an iterated induced graph with a single one

An iterated induced graph is isomorphic to the graph induced by any injection with the same
range as the composite.

Formalized by `StatMech.FK.qp_comapComapIso`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-comap-comap-iso).

## Iterated and single induced graphs share the FK partition function

An iterated induced graph has the FK partition function of the graph induced by any injection
with the same range.

Formalized by `StatMech.FK.qp_fkZ_comapComap`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-fk-z-comap-comap).

## Left part of a tag split has the block partition function

The left part of the restriction to `insert τ S`, split by tag `τ`, has the partition function
of the block of `τ`.

Formalized by `StatMech.FK.qp_left_eq`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-left-eq).

## Right part of a tag split has the restricted partition function

The right part of the restriction to `insert τ S`, split by tag `τ`, has the partition
function of the restriction to `S`.

Formalized by `StatMech.FK.qp_right_eq`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-right-eq).

## Interface edges of a split are at most the straddling edges

The interface of the left/right split by `P` has at most as many edges as there are edges
straddling `P`.

Formalized by `StatMech.FK.qp_interface_le_straddle`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-interface-le-straddle).

## Restriction does not increase straddling edges of a tag

Restricting to `insert τ S` does not increase the number of edges straddling tag `τ`.

Formalized by `StatMech.FK.qp_restG_straddle_le`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-rest-g-straddle-le).

## FK partition function of a graph with no vertices is one

The FK partition function of a graph with no vertices is `1`.

Formalized by `StatMech.FK.qp_fkZ_empty`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 292](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L292). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-fk-z-empty).

## Negative log of the ambient FK normalizer

The negative log ambient normalizer `-log (fkZ G p q)`, including unused coordinates.

Formalized by `StatMech.FK.qp_ambientNegLogZ`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 312](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L312). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-ambient-neg-log-z).

## Peeling bound for $-\log Z$ of a tagged graph

Peeling: `-log Z` of the restriction to `S` is at most the sum over `τ ∈ S` of `-log Z` of the
blocks plus `I · (-log (1 - p))`, with `I` at most the number of edges straddling the tags in
`S`.

Formalized by `StatMech.FK.qp_peel_le`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 318](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L318). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-peel-le).

## Ordered nearest-neighbour pairs of $\Lambda_n$ in direction $i$

The ordered nearest-neighbor pairs of `Λ_n` that differ in coordinate `i`.

Formalized by `StatMech.FK.EdgeCount.edgeAxisI`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 372](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L372). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#edge-axis-i).

## Sites of $\Lambda_n$ whose shift in coordinate $i$ stays in the box

The sites of `Λ_n` whose shift by `b` in coordinate `i` stays in `Λ_n`.

Formalized by `StatMech.FK.EdgeCount.shiftDom`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 375](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L375). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#shift-dom).

## Shift map $x \mapsto (x, x + b e_i)$

The ordered pair `(x, x + b e_i)`.

Formalized by `StatMech.FK.EdgeCount.shiftMap`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 378](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L378). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#shift-map).

## A site is adjacent to its unit shift in one coordinate

A site is adjacent to its shift by `±1` in one coordinate.

Formalized by `StatMech.FK.EdgeCount.shift_adj`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 382](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L382). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#shift-adj).

## $2n(2n+1)^{d-1}$ sites of $\Lambda_n$ stay inside after a unit shift

For `b = ±1`, `2n (2n + 1)^{d-1}` sites of `Λ_n` stay in `Λ_n` after the shift.

Formalized by `StatMech.FK.EdgeCount.card_shiftDom`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 391](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L391). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#card-shift-dom).

## Unit shifts of sites staying in the box are pairs in direction $i$

For `b = ±1`, the shift of a site that stays in the box gives a pair in direction `i`.

Formalized by `StatMech.FK.EdgeCount.shiftMap_mem`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 434](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L434). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#shift-map-mem).

## Injectivity of the shift map

The shift map is injective.

Formalized by `StatMech.FK.EdgeCount.shiftMap_inj`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 447](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L447). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#shift-map-inj).

## Pairs in direction $i$ are the forward and backward shifts

The pairs in direction `i` are the forward and the backward shifts.

Formalized by `StatMech.FK.EdgeCount.edgeAxisI_eq`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 451](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L451). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#edge-axis-i-eq).

## Forward and backward shift pairs are disjoint

Forward and backward pairs in one direction are disjoint.

Formalized by `StatMech.FK.EdgeCount.fwd_bwd_disjoint`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 508](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L508). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#fwd-bwd-disjoint).

## $\Lambda_n$ has $4n(2n+1)^{d-1}$ ordered pairs in each direction

There are `2 · 2n (2n + 1)^{d-1}` ordered pairs in each direction.

Formalized by `StatMech.FK.EdgeCount.card_edgeAxisI`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 524](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L524). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#card-edge-axis-i).

## Ordered neighbour pairs of $\Lambda_n$ as a union over directions

The ordered nearest-neighbor pairs of `Λ_n` are the union over directions.

Formalized by `StatMech.FK.EdgeCount.edgeF_biUnion`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 533](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L533). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#edge-f-bi-union).

## Ordered pairs in different directions are disjoint

Pairs in different directions are disjoint.

Formalized by `StatMech.FK.EdgeCount.edgeAxis_disjoint`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 547](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L547). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#edge-axis-disjoint).

## $\Lambda_n$ has $4dn(2n+1)^{d-1}$ ordered nearest-neighbour pairs

The box `Λ_n` has `d · 2 · 2n (2n + 1)^{d-1}` ordered nearest-neighbor pairs.

Formalized by `StatMech.FK.EdgeCount.edgeCard_eq`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 570](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L570). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#edge-card-eq).

## $\Lambda_n$ has $d \cdot 2n(2n+1)^{d-1}$ edges

The box `Λ_n` has `d · 2n (2n + 1)^{d-1}` edges.

Formalized by `StatMech.FK.EdgeCount.boxGraph_edgeCard`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 579](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L579). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#box-graph-edge-card).

## Translation vector onto an orthant of $\Lambda_{2K+1}$

The translation vector `(±(K + 1))_i` that moves `Λ_K` onto the orthant with sign pattern
`s`.

Formalized by `StatMech.FK.qp_vshift`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 600](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L600). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-vshift).

## $|x| \le n$ iff $-n \le x \le n$ for an integer $x$

`|x| ≤ n` for an integer, written with `natAbs`.

Formalized by `StatMech.FK.qp_natAbs_iff`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 604](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L604). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-nat-abs-iff).

## Orthant tag of a site of $\Lambda_{2K+1}$

The orthant tag of a site of `Λ_{2K+1}`: `none` on a coordinate hyperplane, otherwise its sign
pattern.

Formalized by `StatMech.FK.qp_boxTag`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 610](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L610). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-box-tag).

## Coordinate description of the sites with a given orthant tag

A site has tag `s` iff each coordinate lies in `[1, 2K + 1]` or `[-(2K + 1), -1]` according to
`s`.

Formalized by `StatMech.FK.qp_boxTag_some_iff`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 615](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L615). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-box-tag-some-iff).

## Translation of $\Lambda_K$ onto an orthant block of $\Lambda_{2K+1}$

The translation of `Λ_K` onto the sites of `Λ_{2K+1}` with tag `s`.

Formalized by `StatMech.FK.qp_quadφ`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 652](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L652). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-quad).

## Orthant blocks have the FK partition function of $\Lambda_K$

Each orthant block of `Λ_{2K+1}` has the FK partition function of `Λ_K`.

Formalized by `StatMech.FK.qp_block_fkZ`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 674](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L674). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-block-fk-z).

## Hyperplane set of $\Lambda_{2K+1}$

The hyperplane set: sites of `Λ_{2K+1}` with some coordinate equal to `0`.

Formalized by `StatMech.FK.qp_Jset`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 691](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L691). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-jset).

## Coordinate slab of $\Lambda_{2K+1}$

The sites of `Λ_{2K+1}` with coordinate `i` equal to `0`.

Formalized by `StatMech.FK.qp_Jslab`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 695](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L695). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-jslab).

## Hyperplane set lies in the union of the coordinate slabs

The hyperplane set is the union of the coordinate slabs.

Formalized by `StatMech.FK.qp_Jset_subset_biUnion`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 699](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L699). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-jset-subset-bi-union).

## A coordinate slab has at most $(4K+3)^{d-1}$ sites

Each coordinate slab has at most `(4K + 3)^{d-1}` sites.

Formalized by `StatMech.FK.qp_Jslab_card`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 708](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L708). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-jslab-card).

## The hyperplane set has at most $d(4K+3)^{d-1}$ sites

The hyperplane set has at most `d (4K + 3)^{d-1}` sites.

Formalized by `StatMech.FK.qp_Jset_card_le`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 744](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L744). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-jset-card-le).

## Vertex degrees in a box are at most $2d$

Every vertex of a box has degree at most `2d`. See also
`MathlibExt...PlanarTopology.degree_le` for `ℤ^d`.

Formalized by `StatMech.FK.qp_boxGraph_degree_le`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 757](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L757). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-box-graph-degree-le).

## An edge leaving an orthant ends on a coordinate hyperplane

An edge leaving an orthant has an endpoint on a coordinate hyperplane.

Formalized by `StatMech.FK.qp_straddle_endpoint_in_J`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 787](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L787). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-straddle-endpoint-in-j).

## Untagged sites are exactly those on a coordinate hyperplane

A site has tag `none` iff it lies on a coordinate hyperplane.

Formalized by `StatMech.FK.qp_tag_none_iff`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 839](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L839). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-tag-none-iff).

## An edge between differently tagged sites meets a coordinate hyperplane

An edge between sites of different tags has an endpoint on a coordinate hyperplane.

Formalized by `StatMech.FK.qp_straddle_endpoint_in_J_all`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 847](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L847). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-straddle-endpoint-in-j-all).

## Edges straddling a tag are incident to the hyperplane set

The edges straddling a tag are incident to the hyperplane set.

Formalized by `StatMech.FK.qp_straddle_subset_all`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 856](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L856). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-straddle-subset-all).

## At most $2d|J|$ edges straddle an orthant tag

At most `2d |J|` edges straddle a tag.

Formalized by `StatMech.FK.qp_straddle_card_le_all`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 885](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L885). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-straddle-card-le-all).

## The hyperplane block has at most $2d|J|$ edges

The hyperplane block has at most `2d |J|` edges.

Formalized by `StatMech.FK.qp_blkNone_edge_le`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 900](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L900). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-blk-none-edge-le).

## Isomorphism from the all-tag restriction to $\Lambda_{2K+1}$

The restriction of `Λ_{2K+1}` to all tags is `Λ_{2K+1}`.

Formalized by `StatMech.FK.qp_restGUnivIso`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 938](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L938). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-rest-guniv-iso).

## The all-tag restriction has the partition function of $\Lambda_{2K+1}$

The restriction to all tags has the partition function of `Λ_{2K+1}`.

Formalized by `StatMech.FK.qp_restG_univ_fkZ`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 944](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L944). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-rest-g-univ-fk-z).

## Doubling inequality for $-\log Z$ of the free $q = 2$ FK model

The doubling inequality `u(2K + 1) ≤ 2^d u(K) + I_K · (-log (1 - p))` for `u = -log Z` of the
free `q = 2` FK model, with `I_K = (2^d + 2) · 2d |J|`.

Formalized by `StatMech.FK.qp_box_neglog_doubling`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 951](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L951). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-box-neglog-doubling).

## $\Lambda_{2K+1}$ has at least $2^d$ times as many edges as $\Lambda_K$

The `2^d` orthant copies of `Λ_K` have at most as many edges as `Λ_{2K+1}`.

Formalized by `StatMech.FK.qp_edge_le`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 1014](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L1014). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-edge-le).

## Bound on the edge gap $|E(\Lambda_{2K+1})| - 2^d |E(\Lambda_K)|$

The edge-number gap `|E(Λ_{2K+1})| - 2^d |E(Λ_K)|` is at most `d (d + 2)(4K + 3)^{d-1}`.

Formalized by `StatMech.FK.qp_edge_gap_le`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 1033](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L1033). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-edge-gap-le).

## Lower bound $n(2n+1)^{d-1}$ on the number of edges of $\Lambda_n$

The box `Λ_n` has at least `n (2n + 1)^{d-1}` edges.

Formalized by `StatMech.FK.qp_edge_lower`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 1092](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L1092). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-edge-lower).

## Summability of doubling corrections relative to edge counts

Corrections of order `K_j^{d-1}` divided by `|E(Λ_{K_{j+1}})|` are summable along `K_j =
2^{j+1} - 1`.

Formalized by `StatMech.FK.qp_summable_ratio`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 1106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L1106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-summable-ratio).

## Additive doubling bound for $-\log Z$ of the free $q = 2$ FK model

The additive doubling bound for `u = -log Z` of the free `q = 2` FK model along the doubling
boxes `K_j = 2^{j+1} - 1`, in every dimension `d ≥ 1`.

Formalized by `StatMech.FK.qp_additiveDoublingBound`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 1147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L1147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-additive-doubling-bound).

## Box Fekete data from a uniform bound and an oscillation bound

The box Fekete data for the free `q = 2` FK model from a uniform bound on `u / |E|` along
doubling boxes and an oscillation bound between general and doubling boxes.

Formalized by `StatMech.FK.qp_additiveBoxFeketeData`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean, line 1212](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/QuadrantPartition.lean#L1212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#qp-additive-box-fekete-data).

## Random-cluster weight is at most $q^{|V|}$ for $q \ge 1$

For `q ≥ 1` every random-cluster weight is at most `q ^ |V|`. The case `q = 2` is
`ecz_fkWeight_le`.

Formalized by `StatMech.Walls.fkc_fkWeight_le`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxFreeEnergyBound.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/BoxFreeEnergyBound.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#fkc-fk-weight-le).

## Edge partition function is at most $2^{|E|} q^{|V|}$ for $q \ge 1$

For `q ≥ 1` the edge partition function is at most `2 ^ |E| q ^ |V|`. The case `q = 2` is
`ecz_fkZEdge_le`.

Formalized by `StatMech.Walls.fkc_fkZEdge_le`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxFreeEnergyBound.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/BoxFreeEnergyBound.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#fkc-fk-zedge-le).

## Edge-normalized box free energy of the random-cluster model

The edge-normalized free energy of the random-cluster model on the box of side `2n + 1` in
dimension `d`, in the logit parameter `s`: `log Z^E / |E| + log (1 + eˢ)` with
`Z^E = ecz_fkZEdge (boxGraph d n) (fsc_logistic s) q`.

Formalized by `StatMech.Walls.fkc_edgeFreeEnergy`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxFreeEnergyBound.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/BoxFreeEnergyBound.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#fkc-edge-free-energy).

## Uniform upper bound on the box free energy for $d, n, q \ge 1$

For `d, n ≥ 1` and `q ≥ 1` the box free energy is at most `log 2 + 2 log q + log (1 + eˢ)`.
The case `q = 2` is `ecz_edgeFE_le_const`.

Formalized by `StatMech.Walls.fkc_rq_bdd`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxFreeEnergyBound.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/BoxFreeEnergyBound.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#fkc-rq-bdd).

## Box free energy $-\log Z^E$ of the random-cluster model

The box free energy `-log Z^E` of the random-cluster model on `[-n, n]^d` at edge parameter
`fsc_logistic s`, over configurations closed off the box edges.

Formalized by `StatMech.Walls.fkc_u`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxVanHoveLimit.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/BoxVanHoveLimit.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#fkc-u).

## Per-edge box free energy

The per-edge box free energy `fkc_u / |E|`.

Formalized by `StatMech.Walls.fkc_f`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxVanHoveLimit.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/BoxVanHoveLimit.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#fkc-f).

## Doubling bound for the box free energy when $q \ge 1$

Doubling bound: the free energy of the box of side `2(2K + 1) + 1` is at most `2^d` times that
of side `2K + 1` plus `-log (1 - p)` times the number of boundary edges.

Formalized by `StatMech.Walls.fkc_box_neglog_doubling`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxVanHoveLimit.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/BoxVanHoveLimit.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#fkc-box-neglog-doubling).

## Van Hove subadditivity of the box free energy for $q \ge 1$

Van Hove subadditivity: packing `T^d` copies of the side-`(2m + 1)` box into the
side-`(2n + 1)` box, the free energy is at most `T^d fkc_u m` plus `-log (1 - p)` per remaining
edge.

Formalized by `StatMech.Walls.fkc_box_vanHove_subadd`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxVanHoveLimit.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/BoxVanHoveLimit.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#fkc-box-van-hove-subadd).

## Doubling-bound property of the box free energy along $K_j$

A doubling bound along the dyadic sides `agl_K j` with nonnegative errors `I j` whose
per-edge values are summable.

Formalized by `StatMech.Walls.fkc_AdditiveDoublingBound`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxVanHoveLimit.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/BoxVanHoveLimit.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#fkc-additive-doubling-bound).

## Box free-energy doubling bound along $K_j$ holds for $d, q \ge 1$

The doubling bound holds for all `q ≥ 1`.

Formalized by `StatMech.Walls.fkc_additiveDoublingBound`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxVanHoveLimit.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/BoxVanHoveLimit.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#fkc-additive-doubling-bound-2).

## Per-edge free energy converges along $K_j$ for $d, q \ge 1$

The per-edge free energy converges along the dyadic sides `agl_K j`.

Formalized by `StatMech.Walls.fkc_dyadic_f_tendsto`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxVanHoveLimit.lean, line 337](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/BoxVanHoveLimit.lean#L337). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#fkc-dyadic-f-tendsto).

## Convergence of the per-edge box free energy

The per-edge box free energy `fkc_f d s q n` converges as `n → ∞`.

Formalized by `StatMech.Walls.fkc_PerEdgeDensityConverges`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxVanHoveLimit.lean, line 424](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/BoxVanHoveLimit.lean#L424). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#fkc-per-edge-density-converges).

## Limit of the van Hove upper bound for a fixed box side

The limit of the van Hove upper bound for a fixed side `2m + 1`.

Formalized by `StatMech.Walls.fkc_g`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxVanHoveLimit.lean, line 470](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/BoxVanHoveLimit.lean#L470). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#fkc-g).

## Van Hove limit

**Van Hove limit** of the random-cluster free energy: for `d ≥ 1` and `q ≥ 1`, the per-edge
free energy on the box `[-n, n]^d` converges. See D. Ruelle, *Statistical Mechanics: Rigorous
Results* (1969), and G. Grimmett, *The Random-Cluster Model* (2006), Chapter 4.

Formalized by `StatMech.Walls.fkc_perEdgeDensityConverges`, a theorem declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxVanHoveLimit.lean, line 519](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/BoxVanHoveLimit.lean#L519). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html#fkc-per-edge-density-converges-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Free energy of the random-cluster model](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/random-cluster-model/free-energy-of-the-random-cluster-model)
