---
declaration: section
origin: cited
lean: StatMech.FK.boxSecantSurface, StatMech.FK.boxSecantVolume, StatMech.FK.connectedComponent_card_le_add_of_sup, StatMech.FK.pressureRightDeriv, StatMech.FK.pressureLeftDeriv, StatMech.FK.pressureLeftDeriv_le_rightDeriv, StatMech.FK.countable_leftDeriv_ne_rightDeriv, StatMech.FK.pressure_convex_countable_density_ne
statement: formalized
proof: formalized
---

# Convexity of the free energy and edge densities

72 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html).

## Surface count of a box

The surface count `2d (2n + 1)^{d - 1}` of the box `Λ_n`.

Formalized by `StatMech.FK.boxSecantSurface`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWiredClusterCount.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWiredClusterCount.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#box-secant-surface).

## Edge-volume count of a box

The edge-volume count `d (2n + 1)^d` of the box `Λ_n`.

Formalized by `StatMech.FK.boxSecantVolume`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWiredClusterCount.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWiredClusterCount.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#box-secant-volume).

## Adding edges within a vertex set drops components by at most its size

Adding edges with both endpoints in `{v | p v}` lowers the number of connected components by at
most `|{v | p v}|`. See also `card_connectedComponent_le_sup_fromEdgeSet` (`EdgeMarginal`) for
the
bound by the number of added edges.

Formalized by `StatMech.FK.connectedComponent_card_le_add_of_sup`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWiredClusterCount.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWiredClusterCount.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#connected-component-card-le-add-of-sup).

## Right derivative of the pressure

The right derivative `g'₊(x) = derivWithin g (Ioi x) x`, the form used by Mathlib's
`ConvexOn.monotoneOn_rightDeriv`.

Formalized by `StatMech.FK.pressureRightDeriv`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PressureDiff.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PressureDiff.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#pressure-right-deriv).

## Left derivative of the pressure

The left derivative `g'₋(x) = derivWithin g (Iio x) x`.

Formalized by `StatMech.FK.pressureLeftDeriv`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PressureDiff.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PressureDiff.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#pressure-left-deriv).

## Left derivative of a convex function is at most the right one

`g'₋(x) ≤ g'₊(x)`; Mathlib's `ConvexOn.leftDeriv_le_rightDeriv_of_mem_interior` on `univ`.

Formalized by `StatMech.FK.pressureLeftDeriv_le_rightDeriv`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PressureDiff.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PressureDiff.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#pressure-left-deriv-le-right-deriv).

## Convex function has equal one-sided derivatives off a countable set

A convex function on `ℝ` has equal left and right derivatives off a countable set.

Formalized by `StatMech.FK.countable_leftDeriv_ne_rightDeriv`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PressureDiff.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PressureDiff.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#countable-left-deriv-ne-right-deriv).

## Derivative marginals of a convex pressure agree off a countable set

If two families of edge marginals are the left and right derivatives of a convex `g`, they
differ only on a countable set of parameters.

Formalized by `StatMech.FK.pressure_convex_countable_density_ne`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PressureDiff.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PressureDiff.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#pressure-convex-countable-density-ne).

## Coupled measures agree off a countable set, given a convex pressure

If `μ p` and `ν p` are monotonically coupled, the edge density of `ν p` at `e` is the right
derivative of a convex `g`, and all edge marginals agree wherever that density is continuous in
`p`, then `μ p` and `ν p` agree on every increasing event for `p` off a countable set.

Formalized by `StatMech.FK.fk_uniqueness_of_pressure_convex`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PressureDiff.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PressureDiff.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#fk-uniqueness-of-pressure-convex).

## Set where coupled measures differ is countable under a convex pressure

The set of parameters at which `μ p` and `ν p` differ on some increasing event is countable,
under the hypotheses of `fk_uniqueness_of_pressure_convex`.

Formalized by `StatMech.FK.countable_phi_ne_of_pressure_convex`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PressureDiff.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PressureDiff.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#countable-phi-ne-of-pressure-convex).

## Logistic function $e^t/(1+e^t)$

The logistic map `t ↦ eᵗ / (1 + eᵗ)`, equal to Mathlib's `Real.sigmoid`
(`fsc_logistic_eq_sigmoid`).

Formalized by `StatMech.FK.fsc_logistic`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/LogitFreeEnergyComparison.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/LogitFreeEnergyComparison.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#fsc-logistic).

## Logit function $\log(p/(1-p))$

The logit `p ↦ log (p / (1 - p))`, inverse to `fsc_logistic` on `(0, 1)`.

Formalized by `StatMech.FK.fsc_logit`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/LogitFreeEnergyComparison.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/LogitFreeEnergyComparison.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#fsc-logit).

## Logistic function equals the sigmoid

The logistic map is Mathlib's `Real.sigmoid`.

Formalized by `StatMech.FK.fsc_logistic_eq_sigmoid`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/LogitFreeEnergyComparison.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/LogitFreeEnergyComparison.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#fsc-logistic-eq-sigmoid).

## Convex free-energy hypothesis for a box edge at $q = 2$

The convex free-energy hypothesis for the box edge `eb` at `q = 2`: some convex `g` has
right derivative `t ↦ θ^w(fsc_logistic t)` and left derivative `t ↦ θ^f(fsc_logistic t)`, the wired
and free infinite-volume densities of the edge.

Formalized by `StatMech.FK.fsc_FreeEnergyData`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/LogitFreeEnergyComparison.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/LogitFreeEnergyComparison.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#fsc-free-energy-data).

## Convex free energy gives wired density at $p'$ at most free at $p > p'$

Under `fsc_FreeEnergyData`, the wired edge density at `p'` is at most the free edge density
at `p` whenever `p' < p`.

Formalized by `StatMech.FK.fsc_secant`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/LogitFreeEnergyComparison.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/LogitFreeEnergyComparison.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#fsc-secant).

## Softplus function $\log(1+e^t)$

The softplus function `t ↦ log (1 + eᵗ)`.

Formalized by `StatMech.FK.fsc_softplus`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/LogitFreeEnergyComparison.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/LogitFreeEnergyComparison.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#fsc-softplus).

## Softplus is convex with both one-sided derivatives logistic

Softplus is a convex function whose one-sided derivatives are both `fsc_logistic`, so the
derivative conditions in `fsc_FreeEnergyData` can hold for some convex function.

Formalized by `StatMech.FK.fsc_freeEnergyData_satisfiable`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/LogitFreeEnergyComparison.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/LogitFreeEnergyComparison.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#fsc-free-energy-data-satisfiable).

## Edge-marginal uniqueness off a countable set from convex free energy

Under `fsc_FreeEnergyData`, at `q = 2` there is a countable set `S` of parameters off which
every measure `φ` whose box-edge marginal lies between the free and wired ones has the same
marginal as both.

Formalized by `StatMech.FK.fk_uniqueness_q2_secant_from_freeEnergyData`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/LogitFreeEnergyComparison.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/LogitFreeEnergyComparison.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#fk-uniqueness-q2-secant-from-free-energy).

## Free edge densities on a box as left derivatives

The free `q = 2` density of every edge of `Λ_N` at `p = logistic(t)` is the left derivative of
`g`
at `t`.

Formalized by `StatMech.FK.fdd_FreeDensityIsLeftDeriv`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FKDensityDeriv.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FKDensityDeriv.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#fdd-free-density-is-left-deriv).

## Wired edge densities on a box as right derivatives

The wired `q = 2` density of every edge of `Λ_N` at `p = logistic(t)` is the right derivative
of
`g` at `t`.

Formalized by `StatMech.FK.fdd_WiredDensityIsRightDeriv`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FKDensityDeriv.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FKDensityDeriv.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#fdd-wired-density-is-right-deriv).

## Wired edge densities on a box bounded by right derivatives

The wired `q = 2` density of every edge of `Λ_N` at `p = logistic(t)` is at most the right
derivative of `g` at `t`.

Formalized by `StatMech.FK.fdd_WiredDensityUpperBound`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FKDensityDeriv.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FKDensityDeriv.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#fdd-wired-density-upper-bound).

## Average edge density of the $q = 2$ random-cluster measure

The average edge density `|E|^{-1} E_{φ_{G,p,2}}[#open edges]` at `p = logistic(t)`.

Formalized by `StatMech.FK.fpd_avgDensity`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FKPressureDeriv.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FKPressureDeriv.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#fpd-avg-density).

## Collapse of average edge densities to the free density

The average edge densities of the graphs `Gn n` converge to the free infinite-volume `q = 2`
density of every edge of `Λ_N`, at every `t`.

Formalized by `StatMech.FK.fpd_AvgDensityCollapse`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FKPressureDeriv.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FKPressureDeriv.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#fpd-avg-density-collapse).

## Infinite-volume edge densities as one-sided derivatives

The wired and free `q = 2` infinite-volume densities of every edge of `Λ_N` at `p =
logistic(t)`
are the right and left derivatives of `g` at `t`.

Formalized by `StatMech.FK.fpd_IVDensityIsOneSidedDeriv`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FKPressureDeriv.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FKPressureDeriv.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#fpd-ivdensity-is-one-sided-deriv).

## Weighted exponential sum

The exponential sum `S₀(t) = ∑_i w_i e^{a_i t}`.

Formalized by `StatMech.FK.ivp2_Ssum`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/IVPressureConvex.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/IVPressureConvex.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#ivp2-ssum).

## First moment exponential sum

The first moment sum `S₁(t) = ∑_i w_i a_i e^{a_i t}`, the derivative of `S₀`.

Formalized by `StatMech.FK.ivp2_S1`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/IVPressureConvex.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/IVPressureConvex.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#ivp2-s1).

## Second moment exponential sum

The second moment sum `S₂(t) = ∑_i w_i a_i² e^{a_i t}`, the derivative of `S₁`.

Formalized by `StatMech.FK.ivp2_S2`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/IVPressureConvex.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/IVPressureConvex.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#ivp2-s2).

## Cauchy–Schwarz inequality for weighted exponential sums

Cauchy–Schwarz for the exponential sums: `S₁² ≤ S₂ S₀`.

Formalized by `StatMech.FK.ivp2_cauchy_schwarz_cgf`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/IVPressureConvex.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/IVPressureConvex.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#ivp2-cauchy-schwarz-cgf).

## Log-sum-exp cumulant generating function

The log-sum-exp function `K(t) = log ∑_i w_i e^{a_i t}`, the cumulant generating function of
`a` under the weights `w`.

Formalized by `StatMech.FK.ivp2_Kcgf`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/IVPressureConvex.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/IVPressureConvex.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#ivp2-kcgf).

## Convexity of log-sum-exp with nonnegative nonzero weights

A cumulant generating function is convex.

Formalized by `StatMech.FK.ivp2_Kcgf_convexOn`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/IVPressureConvex.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/IVPressureConvex.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#ivp2-kcgf-convex-on).

## Ambient tilted log normalizer of a finite graph

The ambient logit normalizer `|E|⁻¹ log (fkZ G p q) + log (1 + eᵗ)`,
with `p = fsc_logistic t`. For `|E| > 0`, the added term removes the Bernoulli denominator,
not the unused-coordinate factor in `fkZ`. At zero edges this definition uses totalized
real division and equals `log (1 + eᵗ)`; no per-edge physical interpretation is intended.

Formalized by `StatMech.FK.ivp2_ambientTiltLogZ`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/IVPressureConvex.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/IVPressureConvex.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#ivp2-ambient-tilt-log-z).

## Convexity of the ambient tilted log normalizer

The finite-volume ambient tilted log normalizer is convex in `t`.

Formalized by `StatMech.FK.ivp2_ambientTiltLogZ_convexOn`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/IVPressureConvex.lean, line 271](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/IVPressureConvex.lean#L271). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#ivp2-ambient-tilt-log-z-convex-on).

## Pointwise limits of convex functions are convex

A pointwise limit of convex functions on `ℝ` along a nontrivial filter is convex.

Formalized by `StatMech.FK.ivp2_convexOn_of_tendsto`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/IVPressureConvex.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/IVPressureConvex.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#ivp2-convex-on-of-tendsto).

## Limits of ambient tilted log normalizers are convex

Every pointwise limit of finite-volume ambient tilted log normalizers along a nontrivial filter
 is convex.

Formalized by `StatMech.FK.ivp2_limitAmbientTiltLogZ_convexOn`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/IVPressureConvex.lean, line 309](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/IVPressureConvex.lean#L309). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#ivp2-limit-ambient-tilt-log-z-convex-on).

## Pointwise limits of convex maps are convex with one-sided derivatives

A pointwise limit `g` of convex functions on `ℝ` is convex; its one-sided derivatives exist,
are
monotone, are one-sided limits of slopes, and agree off a countable set; slopes of the
approximants converge to slopes of `g`.

Formalized by `StatMech.FK.cdl_convexDerivLimit`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/ConvexDerivLimit.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/ConvexDerivLimit.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#cdl-convex-deriv-limit).

## Continuity of the logistic map

The logistic map `t ↦ e^t / (1 + e^t)` is continuous. It equals Mathlib's `Real.sigmoid`.

Formalized by `StatMech.FK.osc_fsc_logistic_continuous`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OneSidedContinuity.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/OneSidedContinuity.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#osc-fsc-logistic-continuous).

## Continuity in $p$ of the Bernoulli edge weight

The Bernoulli edge weight of a fixed configuration is continuous in `p`.

Formalized by `StatMech.FK.osc_edgeProduct_continuous`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OneSidedContinuity.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/OneSidedContinuity.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#osc-edge-product-continuous).

## Continuity in $t$ of free $q = 2$ edge marginals on a finite graph

The edge marginal of the free `q = 2` FK measure on a finite graph is continuous in `t`.

Formalized by `StatMech.FK.osc_freeBoxMarg_continuous`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OneSidedContinuity.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/OneSidedContinuity.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#osc-free-box-marg-continuous).

## Continuity in $t$ of wired $q = 2$ edge marginals on a finite graph

The edge marginal of the wired `q = 2` FK measure on a finite graph is continuous in `t`.

Formalized by `StatMech.FK.osc_wiredBoxMarg_continuous`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OneSidedContinuity.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/OneSidedContinuity.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#osc-wired-box-marg-continuous).

## Monotonicity in $p$ of free $q = 2$ edge marginals on a finite graph

The edge marginal of the free `q = 2` FK measure on a finite graph is monotone in `p`.

Formalized by `StatMech.FK.osc_fkEdgeMarg_monotone_in_p`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OneSidedContinuity.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/OneSidedContinuity.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#osc-fk-edge-marg-monotone-in-p).

## Free $q = 2$ edge density is monotone in $p$ on $(0, 1)$

The free infinite-volume `q = 2` edge density is monotone in `p ∈ (0, 1)`.

Formalized by `StatMech.FK.osc_freeEdgeDensity_q2_monotoneOn`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OneSidedContinuity.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/OneSidedContinuity.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#osc-free-edge-density-q2-monotone-on).

## Free $q = 2$ edge density is monotone in $t$

The free infinite-volume `q = 2` edge density is monotone in `t`.

Formalized by `StatMech.FK.osc_freeEdgeDensity_logistic_monotone`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OneSidedContinuity.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/OneSidedContinuity.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#osc-free-edge-density-logistic-monotone).

## Wired $q = 2$ edge density is monotone in $t$

The wired infinite-volume `q = 2` edge density is monotone in `t`.

Formalized by `StatMech.FK.osc_wiredEdgeDensity_logistic_monotone`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OneSidedContinuity.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/OneSidedContinuity.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#osc-wired-edge-density-logistic-monotone).

## Left-continuity of the free $q = 2$ edge density in $t$

The free infinite-volume `q = 2` edge density is left-continuous in `t`.

Formalized by `StatMech.FK.osc_freeEdgeDensity_left_continuous`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OneSidedContinuity.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/OneSidedContinuity.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#osc-free-edge-density-left-continuous).

## Right-continuity of the wired $q = 2$ edge density in $t$

The wired infinite-volume `q = 2` edge density is right-continuous in `t`.

Formalized by `StatMech.FK.osc_wiredEdgeDensity_right_continuous`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OneSidedContinuity.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/OneSidedContinuity.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#osc-wired-edge-density-right-continuous).

## Non-bulk edge fraction bound from a boundary bound on their count

If the non-bulk edges of `Λ_n` number at most `C` times the boundary of `Λ_n`, their fraction
is at most `C` times the boundary-to-edge ratio.

Formalized by `StatMech.FK.spc_boundaryFraction_le_surfaceVolume`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/SpatialCollapse.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/SpatialCollapse.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#spc-boundary-fraction-le-surface-volume).

## Ambient tilted log normalizer ignores the decidability instance

The per-edge ambient tilted log normalizer does not depend on the decidability instance of the
  adjacency
relation.

Formalized by `StatMech.FK.spc_ambientTiltLogZ_instIrrel`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/SpatialCollapse.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/SpatialCollapse.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#spc-ambient-tilt-log-z-inst-irrel).

## Tilted log normalizers on a fixed box take finitely many values

The per-edge ambient tilted log normalizers of a sequence of graphs on the fixed box `Λ_N` take
  finitely many
values.

Formalized by `StatMech.FK.spc_range_finite`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/SpatialCollapse.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/SpatialCollapse.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#spc-range-finite).

## Limits of tilted log normalizers on a fixed box are attained

A limit of per-edge ambient tilted log normalizers of graphs on the fixed box `Λ_N` is attained
  by one of the
graphs.

Formalized by `StatMech.FK.spc_feketeLimit_mem_finiteRange`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/SpatialCollapse.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/SpatialCollapse.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#spc-fekete-limit-mem-finite-range).

## A limit shared with growing boxes is one fixed-box graph's value

If graphs on the fixed box `Λ_N` and the growing boxes `Λ_n` have the same limiting per-edge
ambient tilted log normalizer `g t`, then `g t` is the ambient tilted log normalizer of a single
  graph on `Λ_N`.

Formalized by `StatMech.FK.spc_fixedBox_collapse_obstruction`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/SpatialCollapse.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/SpatialCollapse.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#spc-fixed-box-collapse-obstruction).

## Volume-growth lemma for tilted finite-volume bounds

If `ε ≤ q ^ (S n) λ ^ (m V n) / ε` for all `n`, with `q ≥ 1`, `0 < λ < 1`, `V n → ∞` and
`S n / V n → 0`, then `m ≤ 0`.

Formalized by `StatMech.FK.secant_exponent_le_zero`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TiltSecant.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TiltSecant.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#secant-exponent-le-zero).

## Tilted finite-volume bounds for all $\varepsilon > 0$ force $b \le a$

If for every `ε > 0` the bound `ε ≤ q ^ (S n) λ ^ ((b - a - 2ε) V n) / ε` holds for all
`n`, with `V n → ∞` and `S n = o(V n)`, then `b ≤ a`.

Formalized by `StatMech.FK.secant_b_le_a_of_finiteVolumeData`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TiltSecant.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TiltSecant.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#secant-b-le-a-of-finite-volume-data).

## Finite-volume tilt data for a box edge at $q = 2$

Finite-volume tilt data for the box edge `eb` at `q = 2`: volumes `V n → ∞` and surface
terms `S n = o(V n)` such that, for all `p' < p` in `(0, 1)` and `ε > 0`,
`ε ≤ 2 ^ (S n) λ ^ ((θ^w(p') - θ^f(p) - 2ε) V n) / ε` with `λ = tiltFactor p p'`, where `θ^w` and
`θ^f` are the wired and free infinite-volume densities of the edge.

Formalized by `StatMech.FK.FKSecantData`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TiltSecant.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TiltSecant.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#fksecant-data).

## Tilt data give wired density at $p'$ at most free density at $p > p'$

Under `FKSecantData`, the wired edge density at `p'` is at most the free edge density at
`p` whenever `p' < p`.

Formalized by `StatMech.FK.hsecant_discharged`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TiltSecant.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TiltSecant.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#hsecant-discharged).

## Box-edge marginal uniqueness off a countable set under tilt data

Under `FKSecantData`, at `q = 2` there is a countable set `S` of parameters off which every
measure `φ` whose box-edge marginal lies between the free and wired ones has the same marginal
as both.

Formalized by `StatMech.FK.fk_uniqueness_q2_secant_from_finiteVolumeData`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TiltSecant.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TiltSecant.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#fk-uniqueness-q2-secant-from-finite-volu).

## Wired per-edge ambient tilted log normalizer

The wired per-edge ambient tilted log normalizer `|E|⁻¹ log Z^w(p, q) + log(1 + e^t)` at `p =
 e^t / (1 + e^t)`.

Formalized by `StatMech.FK.wpd_wiredAmbientTiltLogZ`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredPressureDeriv.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredPressureDeriv.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#wpd-wired-ambient-tilt-log-z).

## Wired partition function at logistic $p$ as a tilted sum

The wired partition function at `p = e^t / (1 + e^t)` as a tilted sum over configurations
divided by `(1 + e^t)^{|E|}`.

Formalized by `StatMech.FK.wpd_wiredFkZ_logistic`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredPressureDeriv.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredPressureDeriv.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#wpd-wired-fk-z-logistic).

## Wired tilted log normalizer as a cumulant generating function

The wired ambient tilted log normalizer is `|E|⁻¹` times the cumulant generating function of the
  number of open
edges under the weight `q^{k^w}`.

Formalized by `StatMech.FK.wpd_wiredAmbientTiltLogZ_eq_Kcgf`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredPressureDeriv.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredPressureDeriv.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#wpd-wired-ambient-tilt-log-z-eq-kcgf).

## Convexity of the wired tilted log normalizer

The wired ambient tilted log normalizer is convex in `t`.

Formalized by `StatMech.FK.wpd_wiredAmbientTiltLogZ_convexOn`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredPressureDeriv.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredPressureDeriv.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#wpd-wired-ambient-tilt-log-z-convex-on).

## Expectation under the wired FK measure

The expectation of an observable under the wired FK measure.

Formalized by `StatMech.FK.wpd_wiredFkExpect`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredPressureDeriv.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredPressureDeriv.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#wpd-wired-fk-expect).

## Tilted mean of open edges equals the wired FK expectation

The tilted mean of the number of open edges is its wired FK expectation.

Formalized by `StatMech.FK.wpd_wiredCgfMean_eq_openCount_expect`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredPressureDeriv.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredPressureDeriv.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#wpd-wired-cgf-mean-eq-open-count-expect).

## Wired tilted log normalizer has derivative the mean open fraction

The derivative in `t` of the wired ambient tilted log normalizer is `|E|⁻¹` times the expected
  number of open
edges under the wired FK measure.

Formalized by `StatMech.FK.wpd_wiredAmbientTiltLogZ_hasDerivAt`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredPressureDeriv.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredPressureDeriv.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#wpd-wired-ambient-tilt-log-z-has-deriv-a).

## Average wired edge density

The average wired edge density `|E|⁻¹ E^w[|ω|]` at `p = e^t / (1 + e^t)`.

Formalized by `StatMech.FK.wpd_avgWiredDensity`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredPressureDeriv.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredPressureDeriv.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#wpd-avg-wired-density).

## Expected wired open-edge count is the sum of edge marginals

The expected number of open edges is the sum of the edge marginals.

Formalized by `StatMech.FK.wpd_wiredFkExpect_openCount_eq_sum`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredPressureDeriv.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredPressureDeriv.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#wpd-wired-fk-expect-open-count-eq-sum).

## Average wired edge density as the mean of edge marginals

The average wired edge density is the mean of the wired edge marginals.

Formalized by `StatMech.FK.wpd_avgWiredDensity_eq_sum_edgeMarg`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredPressureDeriv.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredPressureDeriv.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#wpd-avg-wired-density-eq-sum-edge-marg).

## Wired and free FK weights within a factor $q^{|\partial|}$, $q \ge 1$

For `q ≥ 1`, the wired FK weight is at most the free one, and the free one is at most
`q^{|∂|}` times the wired one.

Formalized by `StatMech.FK.wpd_wiredFkWeight_le`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredPressureDeriv.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredPressureDeriv.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#wpd-wired-fk-weight-le).

## Sandwich $Z^w \le Z \le q^{|\partial|} Z^w$ for $q \ge 1$

For `q ≥ 1`, `Z^w ≤ Z ≤ q^{|∂|} Z^w`.

Formalized by `StatMech.FK.wpd_wiredFkZ_le`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredPressureDeriv.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredPressureDeriv.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#wpd-wired-fk-z-le).

## Free-wired log-normalizer gap $\le |\partial|\log q/|E|$ for $q \ge 1$

For `q ≥ 1`, the free and wired per-edge ambient tilted log normalizers differ by at most `|∂|
 log q / |E|`.

Formalized by `StatMech.FK.wpd_ambientTiltLogZ_sub_le`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredPressureDeriv.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredPressureDeriv.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#wpd-ambient-tilt-log-z-sub-le).

## Average wired density collapse at $q = 2$

Average wired density collapse: for every edge `e'` of `Λ_N` and every `t`, the average wired
edge density of `Λ_n` converges to the wired infinite-volume density of `e'`.

Formalized by `StatMech.FK.wpd_AvgWiredDensityCollapse`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredPressureDeriv.lean, line 296](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredPressureDeriv.lean#L296). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#wpd-avg-wired-density-collapse).

## Centered free energy of a graph

The centered free energy `F_G(t) - F_G(0)`, with `F_G = ivp2_ambientTiltLogZ G q`.
In the FK range `q > 0`, the ambient non-edge offset cancels in this difference.

Formalized by `StatMech.FK.cfe_centered`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/CenteredFreeEnergy.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/CenteredFreeEnergy.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#cfe-centered).

## Wired centered free energy

The wired centered free energy, obtained by subtracting
`wpd_wiredAmbientTiltLogZ G bdry q 0` from its value at `t`. In the FK range `q > 0`,
the ambient non-edge offset cancels.

Formalized by `StatMech.FK.cfe_wiredCentered`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/CenteredFreeEnergy.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/CenteredFreeEnergy.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#cfe-wired-centered).

## Pointwise convergence of box centered free energies

The centered free energies of the boxes `Λ_n` converge pointwise to `G`, and `G(0) = 0`.

Formalized by `StatMech.FK.cfe_CenteredConvergence`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/CenteredFreeEnergy.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/CenteredFreeEnergy.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html#cfe-centered-convergence).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Convexity of the free energy and edge densities](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/random-cluster-model/convexity-of-the-free-energy-and-edge-densities)
