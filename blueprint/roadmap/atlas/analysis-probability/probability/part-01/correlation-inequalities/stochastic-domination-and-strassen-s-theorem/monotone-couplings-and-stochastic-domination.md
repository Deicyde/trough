---
declaration: section
origin: cited
lean: StatMech.orderSet, StatMech.MonotoneCoupling, StatMech.MonotoneCoupling.total_mass_eq, StatMech.MonotoneCoupling.stochasticallyDominated, StatMech.stochasticallyDominated_of_exists_monotoneCoupling
statement: formalized
proof: formalized
---

# Monotone couplings and stochastic domination

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/stochastic-domination-and-strassen-s-theorem/monotone-couplings-and-stochastic-domination/index.html).

## Stat Mech

## Set of coordinatewise ordered configuration pairs

The set of ordered pairs `(ω, ω')` of configurations with `ω ≤ ω'` coordinatewise.

Formalized by `StatMech.orderSet`, a definition declared in [MathlibExt/Probability/StochasticOrder/Strassen.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/StochasticOrder/Strassen.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/stochastic-domination-and-strassen-s-theorem/monotone-couplings-and-stochastic-domination/index.html#order-set).

## Monotone coupling of two measures

`κ` is a monotone coupling of `μ` and `ν`: a measure on pairs of configurations with first
marginal `μ`, second marginal `ν`, and no mass off the ordered pairs `ω ≤ ω'`.

Formalized by `StatMech.MonotoneCoupling`, a structure declared in [MathlibExt/Probability/StochasticOrder/Strassen.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/StochasticOrder/Strassen.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/stochastic-domination-and-strassen-s-theorem/monotone-couplings-and-stochastic-domination/index.html#monotone-coupling).

## Marginals of a coupling have equal total mass

The two marginals of a coupling have the same total mass.

Formalized by `StatMech.MonotoneCoupling.total_mass_eq`, a theorem declared in [MathlibExt/Probability/StochasticOrder/Strassen.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/StochasticOrder/Strassen.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/stochastic-domination-and-strassen-s-theorem/monotone-couplings-and-stochastic-domination/index.html#total-mass-eq).

## Strassen's theorem, easy direction

A finite monotone coupling of `μ` and `ν` shows `μ ≼ ν`: the easy direction of Strassen's
theorem.

Formalized by `StatMech.MonotoneCoupling.stochasticallyDominated`, a theorem declared in [MathlibExt/Probability/StochasticOrder/Strassen.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/StochasticOrder/Strassen.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/stochastic-domination-and-strassen-s-theorem/monotone-couplings-and-stochastic-domination/index.html#stochastically-dominated).

## Existence of a monotone coupling implies stochastic domination

If a finite monotone coupling of `μ` and `ν` exists, then `μ ≼ ν`.

Formalized by `StatMech.stochasticallyDominated_of_exists_monotoneCoupling`, a theorem declared in [MathlibExt/Probability/StochasticOrder/Strassen.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/StochasticOrder/Strassen.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/stochastic-domination-and-strassen-s-theorem/monotone-couplings-and-stochastic-domination/index.html#stochastically-dominated-of-exists-monot).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Monotone couplings and stochastic domination](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/stochastic-domination-and-strassen-s-theorem/monotone-couplings-and-stochastic-domination/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/correlation-inequalities/stochastic-domination-and-strassen-s-theorem/monotone-couplings-and-stochastic-domination)
