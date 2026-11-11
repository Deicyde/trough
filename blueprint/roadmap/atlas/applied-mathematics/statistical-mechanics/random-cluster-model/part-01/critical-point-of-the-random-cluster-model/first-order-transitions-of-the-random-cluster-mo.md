---
declaration: section
origin: cited
lean: StatMech.FK.fkThetaFree, StatMech.FK.fkThetaFree_nonneg, StatMech.FK.fkThetaFree_le_one, StatMech.FK.IsFirstOrderTransition, StatMech.FK.firstOrderTransition_of_contour, StatMech.FK.fkThetaFree_ne_fkTheta_of_firstOrder, StatMech.FK.freeInfiniteVolume_ne_wiredInfiniteVolume_of_firstOrder, StatMech.FK.order_transition_q_large
statement: formalized
proof: formalized
---

# First-order transitions of the random-cluster model

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/first-order-transitions-of-the-random-cluster-mo/index.html).

## A. The free percolation probability

## Free percolation probability

The free percolation probability `θ⁰(p, q)`: the free infinite-volume measure of the event that
the origin lies in an infinite open cluster.

Formalized by `StatMech.FK.fkThetaFree`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OrderTransition.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OrderTransition.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/first-order-transitions-of-the-random-cluster-mo/index.html#fk-theta-free).

## Nonnegativity of the free percolation probability

`θ⁰(p, q) ≥ 0`.

Formalized by `StatMech.FK.fkThetaFree_nonneg`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OrderTransition.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OrderTransition.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/first-order-transitions-of-the-random-cluster-mo/index.html#fk-theta-free-nonneg).

## Free percolation probability is at most one

`θ⁰(p, q) ≤ 1`.

Formalized by `StatMech.FK.fkThetaFree_le_one`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OrderTransition.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OrderTransition.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/first-order-transitions-of-the-random-cluster-mo/index.html#fk-theta-free-le-one).

## First-order transition of the random-cluster model

A first-order transition at `(p, q)`: the free measure does not percolate, `θ⁰(p, q) = 0`, while
the wired one does, `θ¹(p, q) > 0`.

Formalized by `StatMech.FK.IsFirstOrderTransition`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OrderTransition.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OrderTransition.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/first-order-transitions-of-the-random-cluster-mo/index.html#is-first-order-transition).

## First-order transition from $\theta^0 = 0$ and $\theta^1 > 0$

Introduction rule for `IsFirstOrderTransition`.

Formalized by `StatMech.FK.firstOrderTransition_of_contour`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OrderTransition.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OrderTransition.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/first-order-transitions-of-the-random-cluster-mo/index.html#first-order-transition-of-contour).

## $\theta^0 \ne \theta^1$ at a first-order transition

At a first-order transition, `θ⁰(p, q) ≠ θ¹(p, q)`.

Formalized by `StatMech.FK.fkThetaFree_ne_fkTheta_of_firstOrder`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OrderTransition.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OrderTransition.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/first-order-transitions-of-the-random-cluster-mo/index.html#fk-theta-free-ne-fk-theta-of-first-order).

## Free and wired measures differ at a first-order transition

At a first-order transition, the free and wired infinite-volume measures differ.

Formalized by `StatMech.FK.freeInfiniteVolume_ne_wiredInfiniteVolume_of_firstOrder`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OrderTransition.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OrderTransition.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/first-order-transitions-of-the-random-cluster-mo/index.html#free-infinite-volume-ne-wired-infinite-v).

## Free and wired measures differ at self-dual $p$ for $q > 4$ if first order

At a point `p ∈ (0, 1)` given as the self-dual point on `ℤ²`, the hypotheses `θ⁰ = 0`
and `θ¹ > 0` give a first-order transition with distinct free and wired measures. The
first-order property for `q > 4` (Duminil-Copin et al., 2021) is assumed, not proved;
`4 < q` is only used to get `q > 0`.

Formalized by `StatMech.FK.order_transition_q_large`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OrderTransition.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OrderTransition.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/first-order-transitions-of-the-random-cluster-mo/index.html#order-transition-q-large).

## Free and wired measures differ at $\sqrt{q}/(1+\sqrt{q})$ for $q > 4$ if first order

`order_transition_q_large` at the self-dual point `p_sd(q) = √q / (1 + √q)` of `ℤ²`, with
`θ⁰(p_sd, q) = 0` and `θ¹(p_sd, q) > 0` assumed.

Formalized by `StatMech.FK.order_transition_q_large_selfDual`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OrderTransition.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OrderTransition.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/first-order-transitions-of-the-random-cluster-mo/index.html#order-transition-q-large-self-dual).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: First-order transitions of the random-cluster model](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/first-order-transitions-of-the-random-cluster-mo/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/first-order-transitions-of-the-random-cluster-mo)
