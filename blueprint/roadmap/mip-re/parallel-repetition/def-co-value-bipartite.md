---
declaration: definition
origin: cited
lean: MIPRE.CommutingOperatorStrategy.value, MIPRE.commutingOperatorValue
statement: formalized
---

# Commuting-operator value

[[$\uparrow$ QuantumLib](https://github.com/Timeroot/Lean-QuantumInfo)] The value of a commuting-operator strategy $\mathscr{S} = (\mathcal{H}, \psi, E, F)$ in $\mathfrak{G}$ is

$$
{\omega^{\mathrm{co}}}(\mathfrak{G}, \mathscr{S}) = \sum_{x, y, a, b} \mu(x,y)\, D(x,y,a,b)\,
\langle\psi| E^x_a F^y_b |\psi\rangle\;,
$$

and the *commuting-operator value* ${\omega^{\mathrm{co}}}(\mathfrak{G})$ of $\mathfrak{G}$ is the supremum of ${\omega^{\mathrm{co}}}(\mathfrak{G}, \mathscr{S})$ over all commuting-operator strategies.

## Depends on

- [Commuting-operator strategy](def-co-strategy-bipartite.md)
- [Nonlocal game](../foundations/part-01/def-game.md)

## Lean

Formalized as [`MIPRE.CommutingOperatorStrategy.value`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CommutingOperatorStrategy.value), [`MIPRE.commutingOperatorValue`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.commutingOperatorValue).

## Sources

- [MIP* = RE blueprint: content/05_parallel_repetition.tex, line 74](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/05_parallel_repetition.tex#L74)
