---
declaration: section
origin: cited
lean: StatMech.Transport.IsDown, StatMech.Transport.OrderPairs, StatMech.Transport.exists_coupling_vec, StatMech.kappaOfVec, StatMech.exists_monotoneCoupling_of_stochasticallyDominated
statement: formalized
proof: formalized
---

# Strassen's theorem for configurations on a finite set

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/stochastic-domination-and-strassen-s-theorem/strassen-s-theorem-for-configurations-on-a-finit/index.html).

## Transport

## Down-set of a partial order

`D` is a down-set of `P`: `x ≤ y` and `y ∈ D` imply `x ∈ D`.

Formalized by `StatMech.Transport.IsDown`, a definition declared in [MathlibExt/Probability/StochasticOrder/StrassenFinite.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/StochasticOrder/StrassenFinite.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/stochastic-domination-and-strassen-s-theorem/strassen-s-theorem-for-configurations-on-a-finit/index.html#is-down).

## Ordered pairs of a partial order

The ordered pairs `(x, y)` with `x ≤ y`; couplings supported on the order are vectors indexed
by `OrderPairs P`.

Formalized by `StatMech.Transport.OrderPairs`, an abbreviation declared in [MathlibExt/Probability/StochasticOrder/StrassenFinite.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/StochasticOrder/StrassenFinite.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/stochastic-domination-and-strassen-s-theorem/strassen-s-theorem-for-configurations-on-a-finit/index.html#order-pairs).

## Strassen's theorem

**Strassen's theorem** on a finite poset `P`, for nonnegative vectors: if `μ` and `ν` have
equal total mass and `ν(D) ≤ μ(D)` for every down-set `D`, there is a nonnegative `c` on the
ordered pairs `x ≤ y` with first marginal `μ` and second marginal `ν`. This is the ordered-pair
vector form of
`MathlibExt.Probability.StrassenCouplingWanted.forall_isUpperSet_sum_le_iff_exists_coupling`.

Formalized by `StatMech.Transport.exists_coupling_vec`, a theorem declared in [MathlibExt/Probability/StochasticOrder/StrassenFinite.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/StochasticOrder/StrassenFinite.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/stochastic-domination-and-strassen-s-theorem/strassen-s-theorem-for-configurations-on-a-finit/index.html#exists-coupling-vec).

## Measure on ordered pairs from a mass vector

The measure on pairs of configurations that puts mass `c q` on each ordered pair `q`.

Formalized by `StatMech.kappaOfVec`, a definition declared in [MathlibExt/Probability/StochasticOrder/StrassenFinite.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/StochasticOrder/StrassenFinite.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/stochastic-domination-and-strassen-s-theorem/strassen-s-theorem-for-configurations-on-a-finit/index.html#kappa-of-vec).

## Strassen's theorem

**Strassen's theorem** for configurations on a finite set: if `μ ≼ ν` are probability
measures on `ConfigSpace E`, there is a finite monotone coupling of `μ` and `ν`
(V. Strassen, *The existence of probability measures with given marginals*, 1965). The converse
is `StatMech.MonotoneCoupling.stochasticallyDominated`.

Formalized by `StatMech.exists_monotoneCoupling_of_stochasticallyDominated`, a theorem declared in [MathlibExt/Probability/StochasticOrder/StrassenFinite.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/StochasticOrder/StrassenFinite.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/stochastic-domination-and-strassen-s-theorem/strassen-s-theorem-for-configurations-on-a-finit/index.html#exists-monotone-coupling-of-stochastical).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Strassen's theorem for configurations on a finite set](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/stochastic-domination-and-strassen-s-theorem/strassen-s-theorem-for-configurations-on-a-finit/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/correlation-inequalities/stochastic-domination-and-strassen-s-theorem/strassen-s-theorem-for-configurations-on-a-finit)
