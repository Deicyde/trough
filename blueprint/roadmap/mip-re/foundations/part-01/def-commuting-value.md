---
declaration: definition
origin: cited
lean: MIPRE.CommutingStrategy.value, MIPRE.commValue
statement: formalized
---

# Commuting value

[[$\uparrow$ QuantumLib](https://github.com/Timeroot/Lean-QuantumInfo)] The value of a commuting strategy $\mathscr{S} = ({\mathscr{A}}, \tau, M)$ in $\mathfrak{G}$ is

$$
{\mathrm{val}^{\mathrm{co}}}(\mathfrak{G}, \mathscr{S}) = \sum_{x, y, a, b} \mu(x,y)\, D(x,y,a,b)\,
\tau\bigl(M^x_a M^y_b\bigr)\;,
$$

and the *commuting value* of $\mathfrak{G}$ is ${\mathrm{val}^{\mathrm{co}}}(\mathfrak{G}) = \sup_\mathscr{S} {\mathrm{val}^{\mathrm{co}}}(\mathfrak{G}, \mathscr{S})$.

## Depends on

- [Commuting strategy](def-commuting-strategy.md)

## Lean

Formalized as [`MIPRE.CommutingStrategy.value`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CommutingStrategy.value), [`MIPRE.commValue`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.commValue).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 198](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L198)
