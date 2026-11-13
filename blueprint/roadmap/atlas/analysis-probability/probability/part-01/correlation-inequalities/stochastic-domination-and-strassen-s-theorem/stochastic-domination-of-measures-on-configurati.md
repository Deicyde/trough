---
declaration: section
origin: cited
lean: StatMech.StochasticallyDominated, StatMech.StochasticallyDominated.refl, StatMech.StochasticallyDominated.trans, StatMech.StochasticallyDominated.real
statement: formalized
proof: formalized
---

# Stochastic domination of measures on configuration space

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/stochastic-domination-and-strassen-s-theorem/stochastic-domination-of-measures-on-configurati/index.html).

## Stochastic domination of measures on configurations

`μ` is stochastically dominated by `ν` if their actual `ENNReal` masses satisfy
`μ(A) ≤ ν(A)` for every measurable increasing event `A ⊆ ConfigSpace E`.

Formalized by `StatMech.StochasticallyDominated`, a definition declared in [MathlibExt/Probability/StochasticOrder/StochasticDomination.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/StochasticOrder/StochasticDomination.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/stochastic-domination-and-strassen-s-theorem/stochastic-domination-of-measures-on-configurati/index.html#stochastically-dominated).

## Stochastic domination is reflexive

Stochastic domination is reflexive.

Formalized by `StatMech.StochasticallyDominated.refl`, a theorem declared in [MathlibExt/Probability/StochasticOrder/StochasticDomination.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/StochasticOrder/StochasticDomination.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/stochastic-domination-and-strassen-s-theorem/stochastic-domination-of-measures-on-configurati/index.html#refl).

## Stochastic domination is transitive

Stochastic domination is transitive.

Formalized by `StatMech.StochasticallyDominated.trans`, a theorem declared in [MathlibExt/Probability/StochasticOrder/StochasticDomination.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/StochasticOrder/StochasticDomination.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/stochastic-domination-and-strassen-s-theorem/stochastic-domination-of-measures-on-configurati/index.html#trans).

## Stochastic domination compares real-valued masses

For a finite upper measure, stochastic domination also compares real-valued masses.

Formalized by `StatMech.StochasticallyDominated.real`, a theorem declared in [MathlibExt/Probability/StochasticOrder/StochasticDomination.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/StochasticOrder/StochasticDomination.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/stochastic-domination-and-strassen-s-theorem/stochastic-domination-of-measures-on-configurati/index.html#real).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Stochastic domination of measures on configuration space](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/stochastic-domination-and-strassen-s-theorem/stochastic-domination-of-measures-on-configurati/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/correlation-inequalities/stochastic-domination-and-strassen-s-theorem/stochastic-domination-of-measures-on-configurati)
